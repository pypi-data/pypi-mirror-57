# scqubits: superconducting qubits in Python
#
# This file is part of scqubits.
#
#     Copyright (c) 2019, Jens Koch and Peter Groszkowski
#     All rights reserved.
#
#     This source code is licensed under the BSD-style license found in the
#     LICENSE file in the root directory of this source tree.
#######################################################################################################################

# core
from scqubits.core.fluxonium import Fluxonium
from scqubits.core.transmon import Transmon
from scqubits.core.zeropi import ZeroPi
from scqubits.core.zeropi_full import FullZeroPi
from scqubits.core.flux_qubit import FluxQubit
from scqubits.core.harmonic_osc import Oscillator
from scqubits.core.hilbert_space import HilbertSpace
from scqubits.core.discretization import Grid1d

# utils
from scqubits.utils.constants import FileType
from scqubits.utils.spectrum_utils import get_matrixelement_table

# version
from scqubits.version import version as __version__


# setup and teardown for nosetests
def setup_package():
    import matplotlib
    import os
    from scqubits.utils.constants import TEMPDIR

    try:
        __IPYTHON__
    except:
        matplotlib.pyplot.switch_backend('agg')   # do not actually show graphics in nosetests

    if not os.path.exists(TEMPDIR):
        try:
            os.mkdir(TEMPDIR)
        except OSError:
            raise RuntimeError('Error creating temporary data directory ' + TEMPDIR)

def teardown_package():
    import shutil
    from scqubits.utils.constants import TEMPDIR
    shutil.rmtree(TEMPDIR)
