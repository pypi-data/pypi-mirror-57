# OCTAVVS: Open Chemometrics Toolbox for Analysis and Visualization of Vibrational Spectroscopy data

OCTAVVS is a set of graphical tools for high-throughput preprocessing and
analysis of vibrational spectroscopy data. Currently, the preprocessing is
primarily geared towards images from infrared absorption spectroscopy with
focal plane array detectors.

There are three separate tools in the current version:

**preprocessing** deals with atmospheric correction, resonant Mie scattering
correction, baseline correction and normalization.

**mcr_als** decomposes observed spectra into nonnegative concentrations and
spectra using the MCR-ALS algorithm.

**clustering** performs K-means clustering on the concentrations inferred by
MCR-ALS.

## Installation on Windows, Mac or Linux

OCCTAVS needs a working Python 3 environment with various packages. The
easiest way to get this is through the Conda package management system.

Download and install the Python 3.7 version of [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
During the installation, Conda may ask about adding its programs to the path,
to which you should probably say no (except on Mac?).

After installing Conda:
* On Windows: Start a Conda console (found in the Start menu).
* On Mac: If you added conda to the path, start Terminal. (Otherwise: ??? Remains to be investigated and explained.)
* On Linux: Start a shell and set the path to include the Conda bin directory. See note at the bottom of this page.

From that console, install OCTAVVS and its dependencies: ``conda install -c ctroein octavvs``

## Finding and using OCTAVVS

The easiest way to access the OCTAVVS tools is through desktop shortcuts
which may be created by running the ``oct_make_icons`` script from the command prompt.
This works on Windows and Linux but has been known to fail on some Mac OS X versions
where icons may look broken and/or clicking on them may do nothing.

Regardless of whether the icons are created, the three scripts
``oct_preprocessing``, ``oct_mcr_als`` and ``oct_clustering``
should be possible to run straight from the console (Conda console or terminal window, as described above).

The location of the OCTAVVS scripts will depend on where you installed Conda.
Within the Conda directory, the files will be located in ``lib/python3.7/site-packages/octavvs``
but the scripts mentioned above will be in ``bin``.

## Test data

Test data from two 64x64 images of _Paxillus_ hyphae growing on lignin can be
[downloaded here](http://cbbp.thep.lu.se/~carl/octavvs/octavvs_test_data.zip) (zip archive, 47 MB).

## Upgrading to the latest version

Information about the most recent release of OCTAVVS can be found on its
[Anaconda Cloud page](https://anaconda.org/ctroein/octavvs), with more details on its
[GitHub page](https://github.com/ctroein/octavvs).

To upgrade, do ``conda update octavvs``

## Bug reports and code repository

Questions, bug reports and other feedback may be sent to corresponding author Carl Troein <carl@thep.lu.se>.

Developers can access the OCTAVVS code through the [OCTAVVS GitHub
page](https://github.com/ctroein/octavvs), where bugs and other issues can
also be reported.


## Installation through pip

Users familiar with Python could also install OCTAVVS through pip as an alternative to Anaconda.
Note that pyqt and opencv sometimes don't work when installed through pip, depending on your system etc.

New releases will be made to the [project page on PyPI](https://pypi.org/project/octavvs/) in parallel with
releases to Anaconda Cloud.


## Linux path problem

On some Linux distributions, notably OpenSUSE, allowing Conda to modify your
$PATH will cause problems with KDE when logging in. If this applies to you,
a suggested workaround is to change the path manually when needed. An alias
in .bashrc can be convenient:  
``alias startconda='export PATH=~/miniconda3/bin:"$PATH"'``
