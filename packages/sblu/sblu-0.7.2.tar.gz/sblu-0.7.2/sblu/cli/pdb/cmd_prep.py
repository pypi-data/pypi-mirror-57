import os
import tempfile
import logging
import subprocess
from itertools import combinations
from collections import OrderedDict

import click
from path import Path
import numpy as np

from sblu import PRMS_DIR
from sblu.pdb import parse_pdb_stream, fix_atom_records
from sblu.util import which

from . import _splitsegs

DISU_THRESH_MIN = 1.28925530695 ** 2
DISU_THRESH_MAX = 2.82114477374 ** 2

logger = logging.getLogger(__name__)


@click.command('prep', short_help="Prepare a PDB file for docking with PIPER.")
@click.option("--clean/--no-clean", "clean_pdb", default=True)
@click.option("--minimize/--no-minimize", default=True)
@click.option("--xplor-psf/--no-xplor-psf", default=False)
@click.option("--smod", default="")
@click.option("--out-prefix")
@click.option("--prm", type=click.Path(exists=True), default=PRMS_DIR/"charmm"/"charmm_param.prm")
@click.option("--rtf", type=click.Path(exists=True), default=PRMS_DIR/"charmm"/"charmm_param.rtf")
@click.option("chains", "--chain", multiple=True)
@click.option("--psfgen", default="psfgen")
@click.option("--nmin", default="nmin")
@click.option("--nsteps", default=1000, type=click.INT)
@click.option("--auto-disu/--no-auto-disu", default=True)
@click.option("--delete-tmp/--no-delete-tmp", default=True)
@click.argument("pdb_file", type=click.File(mode='r'))
def cli(pdb_file, chains, smod, clean_pdb, minimize, prm, rtf, xplor_psf,
        out_prefix, psfgen, nmin, nsteps, auto_disu, delete_tmp):
    def is_cys_sulfur(r):
        return r.name == ' SG ' and r.resname == 'CYS'

    workdir = Path(tempfile.mkdtemp())
    if not workdir:
        workdir = Path(".")
        delete_tmp = False
    else:
        logger.info('created tempdir {}'.format(workdir))

    if not out_prefix:
        out_prefix = "prepared"

    out_prefix = os.path.join(os.path.abspath("."), out_prefix)

    try:
        psfgen_bin = which(psfgen, required=True)

        if clean_pdb:
            records = list(fix_atom_records(parse_pdb_stream(pdb_file,
                                                             only_atoms=True)))
        else:
            records = list(parse_pdb_stream(pdb_file, only_atoms=True))

        all_segments = _splitsegs(records, smod, workdir / "segment")
        is_wildcard = len(chains) == 0 or '?' in chains
        segments = OrderedDict(
            item
            for item in all_segments.items()
            if (item[0][1] in chains or  # chain is explicitly named
                (is_wildcard and item[0][1][0] != 'h'))  # wildcard and not het
        )
        records = list(r
                       for segment in segments.values()
                       for r in parse_pdb_stream(open(segment)))

        p = subprocess.Popen([psfgen_bin],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        commands = []
        commands.append("psfcontext mixedcase")
        commands.append("topology {0}".format(rtf))
        coord_commands = []

        for (segid, chain), segment in segments.items():
            segid = smod + chain + str(segid)

            seg_cmd = "segment {0} {{ first NONE; last NONE; pdb {1} }}".format(
                segid, segment)
            coord_cmd = "coordpdb {0} {1}".format(segment, segid)
            commands.append(seg_cmd)
            coord_commands.append(coord_cmd)

        # Patch noncontinuous chains
        previous_chain = None
        previous_carbon = None
        for (segid, chain), segment in segments.items():
            if previous_chain is not None and previous_chain != chain:
                previous_carbon = None
                previous_chain = chain
                continue

            segment = list(parse_pdb_stream(open(segment, "r")))

            if previous_carbon:
                nitrogen = None
                for record in segment:
                    if record.name == " N  ":
                        nitrogen = record
                        break

                if nitrogen is not None:
                    delta = nitrogen.coords - previous_carbon.coords
                    dist = np.sqrt(np.sum(np.multiply(delta, delta, delta)))
                    if dist < 1.4:
                        link = (previous_carbon.segment.strip(),
                                previous_carbon.resnum,
                                nitrogen.segment.strip(), nitrogen.resnum)

                        if previous_carbon.resname == "GLY":
                            if nitrogen.resname == "GLY":
                                commands.append(
                                    "patch JOGG {}:{} {}:{}".format(*link))
                            elif nitrogen.resname == "PRO":
                                commands.append(
                                    "patch JOGP {}:{} {}:{}".format(*link))
                            else:
                                commands.append(
                                    "patch JOGA {}:{} {}:{}".format(*link))
                        elif nitrogen.resname == "PRO":
                            commands.append("patch JOAP {}:{} {}:{}".format(
                                *link))
                        elif nitrogen.resname == "GLY":
                            commands.append("patch JOAG {}:{} {}:{}".format(
                                *link))
                        else:
                            commands.append("patch JOAA {}:{} {}:{}".format(
                                *link))

            previous_carbon = None
            for record in segment[::-1]:
                if record.name == " C  ":
                    previous_carbon = record
                    break
            previous_chain = chain

        disulfides = []
        if auto_disu:
            for ri, rj in combinations(filter(is_cys_sulfur, records), 2):
                if ri.resnum == rj.resnum and ri.segment == rj.segment:
                    # We might get here if we have two alt-locs of the same sulfur atom
                    continue
                delta = ri.coords - rj.coords
                dist_sq = np.sum(np.multiply(delta, delta, delta))
                if dist_sq > DISU_THRESH_MIN and dist_sq < DISU_THRESH_MAX:
                    disulfides.append((ri.segment.strip(), ri.resnum,
                                       rj.segment.strip(), rj.resnum))

        for link in disulfides:
            commands.append("patch DISU {0}:{1} {2}:{3}".format(*link))

        commands += coord_commands

        commands.append("guesscoord")
        commands.append("writepsf charmm {0}.psf".format(out_prefix))
        if xplor_psf:
            commands.append("writepsf x-plor {0}_xplor.psf".format(out_prefix))
        commands.append("writepdb {0}.pdb".format(out_prefix))

        logger.debug("\n".join(commands))

        stdout, stderr = p.communicate(("\n".join(commands)).encode())

        if minimize and nsteps > 0:
            nmin = which(nmin, required=True)

            input_file = "{0}.pdb".format(out_prefix)
            fixed_atoms_file = workdir / "fixed.pdb"
            with open(input_file, "r") as inp, open(fixed_atoms_file, "w") as out:
                for line in inp:
                    if line.startswith("ATOM") and line[55:60] != ' 0.00':
                        out.write(line)

            cmd = [nmin, "{0}.psf".format(out_prefix), prm, rtf,
                   "{0}.pdb".format(out_prefix), workdir / "fixed.pdb",
                   str(nsteps)]
            with open("{0}_nmin.pdb".format(out_prefix), "w") as min_out:
                subprocess.check_call(cmd, stdout=min_out)
    except:
        logger.exception(
            "Unexpected error: Working files location in {}".format(workdir))
        raise
    else:
        if delete_tmp:
            import shutil
            shutil.rmtree(workdir)
        else:
            print("Working files location in {}".format(workdir))
