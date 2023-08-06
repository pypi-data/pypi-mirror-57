import re
import os
import filecmp
from click.testing import CliRunner
import pytest

from sblu.cli.pdb import cmd_clean, cmd_pdb_psf_concat, cmd_prep

from .. import DATA_DIR

with open(DATA_DIR / "pdb_list") as f:
    PDBS = [l.strip().split() for l in f]

REMARK_RE = re.compile("REMARKS")


def compare_psfs(output, expected):
    with open(output) as o, open(expected) as e:
        output_lines = list(filter(lambda x: not x.isspace(), o.readlines()))
        expected_lines = list(filter(lambda x: not x.isspace(), e.readlines()))
    if len(output_lines) != len(expected_lines):
        return False

    in_atoms = False
    for oline, eline in zip(output_lines, expected_lines):
        if in_atoms:
            if oline[12:] != eline[12:]:
                return False
        else:
            if oline != eline:
                return False

        if "NATOM" in oline:
            in_atoms = True
        if "NBONDS" in oline:
            in_atoms = False
    return True


@pytest.mark.parametrize("pdb,chains", PDBS)
def test_clean(pdb, chains):
    runner = CliRunner()

    with runner.isolated_filesystem():
        input_file = DATA_DIR / 'pdb' / (pdb + '.pdb')
        expected_output = DATA_DIR / 'pdb' / (pdb + '.clean.pdb')

        result = runner.invoke(cmd_clean.cli, [input_file, '--outfile',
                                               'clean.pdb'])
        assert result.exit_code == 0
        assert os.path.exists('clean.pdb')
        assert filecmp.cmp("clean.pdb", expected_output)


@pytest.mark.need_psfgen
def test_concat():
    runner = CliRunner()

    expected_pdb = DATA_DIR / 'pdb' / 'concat' / "reclig.pdb"
    expected_psf = DATA_DIR / 'pdb' / 'concat' / "reclig.psf"

    with runner.isolated_filesystem():
        rtf = (DATA_DIR/"prms"/"prot_na.rtf").relpath()
        params = ["--rtf", rtf]

        inputs = [DATA_DIR / 'pdb' / 'concat' / f for f in ("rec.psf", "rec.pdb", "lig.psf", "lig.pdb")]

        result = runner.invoke(cmd_pdb_psf_concat.cli,
                               ['--prefix', 'output'] + params + inputs)

        assert result.exit_code == 0

        # Remove pesky remark lines
        with open("output.psf") as inp, open("no_remarks.psf", "w") as out:
            for l in inp:
                if not REMARK_RE.search(l):
                    out.write(l)

        assert filecmp.cmp("output.pdb", expected_pdb)

        # In case things don't match, helps to debug
        with open("no_remarks.psf") as x, open(expected_psf) as y:
            a, b = x.read(), y.read()
            if a != b:
                with open("/tmp/x.psf", "w") as o:
                    o.write(a)
        assert filecmp.cmp("no_remarks.psf", expected_psf)


def test_clean_invalid():
    runner = CliRunner()

    result = runner.invoke(cmd_clean.cli, [])
    assert result.exit_code == 2


@pytest.mark.need_psfgen
@pytest.mark.parametrize("pdb,chains", PDBS)
def test_prep(pdb, chains):
    runner = CliRunner()

    with runner.isolated_filesystem():
        prm = (DATA_DIR/"prms"/"prot_na.prm").relpath()
        rtf = (DATA_DIR/"prms"/"prot_na.rtf").relpath()

        input_file = DATA_DIR / 'pdb' / (pdb + '.pdb')
        expected_pdb = DATA_DIR / 'pdb' / (pdb + '_ngen_noseg.pdb')
        expected_psf = DATA_DIR / 'pdb' / (pdb + '_ngen.psf')

        params = ["--prm", prm, "--rtf", rtf]
        for c in chains.split(","):
            params.append("--chain")
            params.append(c)
        params.append("--no-minimize")
        params.append(input_file)
        result = runner.invoke(cmd_prep.cli, params)

        assert result.exit_code == 0
        # Remove pesky remark lines
        with open("prepared.psf") as inp, open("no_remarks.psf", "w") as out:
            for l in inp:
                if not REMARK_RE.search(l):
                    out.write(l)
        # Remove segment
        with open("prepared.pdb") as inp, open("no_segment.pdb", "w") as out:
            for l in inp:
                if l.startswith("ATOM") or l.startswith("HETATM"):
                    out.write(l[:72] + "    " + l[76:])
                else:
                    out.write(l)

        assert filecmp.cmp("no_segment.pdb", expected_pdb)
        assert compare_psfs("no_remarks.psf", expected_psf)
