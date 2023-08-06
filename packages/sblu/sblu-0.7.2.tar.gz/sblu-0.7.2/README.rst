sb-lab-utils
============

Python library and associated scripts for munging data files from
ClusPro/FTMap/etc.

Installation
------------

From PyPI
~~~~~~~~~

Ensure you have ``pip``, then run:

.. code-block:: bash

    [sudo] pip install sblu

From source
~~~~~~~~~~~

First, install psfgen (see below) if you're planning to use ``pdbprep`` functionality.

Clone the repository to your local machine:

.. code-block:: bash

    git clone git@bitbucket.org:bu-structure/sb-lab-utils.git

After cloning, you should be able to install using:

.. code-block:: bash

    cd sb-lab-utils
    [sudo] pip install -r requirements/development.txt
    pytest
    [sudo] python setup.py install

``sudo`` is only needed if you are installing it globally.
We recommend use of Anaconda (https://www.continuum.io).

Requirements
------------

psfgen
~~~~~~

Building PSF files requires psfgen utility from NAMD package.

Download recent precompiled version of NAMD (2.12 Linux-x86_64-multicore) from 
http://www.ks.uiuc.edu/Development/Download/download.cgi?UserID=&AccessCode=&ArchiveID=1501 (registration is required).

Extract the archive and copy the psfgen binary to ``/usr/local/bin/`` (or, if you wish, any other location listed in your **PATH** environment variable):

.. code-block:: bash

    tar zxf NAMD_2.12_Linux-x86_64-multicore.tar.gz && sudo cp NAMD_2.12_Linux-x86_64-multicore/psfgen "/usr/local/bin/"

Python modules
~~~~~~~~~~~~~~

If you're using Anaconda or already have NumPy installed from any other source, 
then you should be fine just running ``pip install -r requirements/development.txt``.

If you don't have NumPy, you might get a cryptic 
``No files/directories in /tmp/pip-install-xxxxx/ProDy/pip-egg-info (from PKG-INFO)`` error during this step.

To resolve it, just install NumPy manually: ``pip install numpy>=1.10``, and then re-run the command above.

Usage
-----

Some basic examples are included in the examples directory.

