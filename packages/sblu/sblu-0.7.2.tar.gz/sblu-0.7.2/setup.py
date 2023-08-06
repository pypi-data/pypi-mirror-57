from os import path
from setuptools import setup


HERE = path.abspath(path.dirname(__file__))

REQUIREMENTS = (
    'path.py >= 7.0',
    'numpy >= 1.10',
    'scipy >= 0.16',
    'configobj >= 5.0',
    'click >= 5.1',
    'requests >= 2.4',
    'prody >= 1.8.2',
    'pyparsing >= 2.3',
    'BioPython >= 1.73'
)

SCRIPTS = (
    'scripts/cl_load_job',
    'scripts/cluspro_local.py',
)

with open(path.join(HERE, "README.rst")) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="sblu",
    packages=['sblu', 'sblu.cli', 'sblu.io',
              'sblu.cli.docking', 'sblu.cli.pdb',
              'sblu.cli.measure', 'sblu.cli.cluspro',
              'sblu.cli.ftmap', 'sblu.cli.atlas',
              'sblu.cli.xyztraj'],
    description="Library for munging data files from ClusPro/FTMap/etc.",
    long_description=LONG_DESCRIPTION,
    url="https://bitbucket.org/bu-structure/sb-lab-utils",
    author="Bing Xia",
    author_email="sixpi@bu.edu",
    license="MIT",
    install_requires=REQUIREMENTS,

    use_scm_version={'write_to': 'sblu/version.py'},
    setup_requires=['setuptools_scm', 'pytest-runner'],

    tests_require=['pytest'],

    scripts=SCRIPTS,
    entry_points={
        'console_scripts': [
            "sblu = sblu.cli.main:cli",
            "pdbget = sblu.cli.pdb.cmd_get:standalone_cli",
            # Prep commands
            "pdbclean = sblu.cli.pdb.cmd_clean:cli",
            "pdbprep = sblu.cli.pdb.cmd_prep:cli",
            # RMSD commands
            "pysrmsd = sblu.cli.measure.cmd_srmsd:cli",
            "pypwrmsd = sblu.cli.measure.cmd_pwrmsd:cli",
            "pyftrmsd = sblu.cli.measure.cmd_ftrmsd:cli"
        ]
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    keywords='cluspro protein PDB'
)
