# testing.py
#
# This file is part of scqubits.
#
#    Copyright (c) 2019, Jens Koch and Peter Groszkowski
#    All rights reserved.
#
#    This source code is licensed under the BSD-style license found in the
#    LICENSE file in the root directory of this source tree.
############################################################################

import nose
import os

from scqubits.utils.constants import TEMPDIR

def run():
    """
    Run the nose test scripts for scqubits.
    """
    # runs tests in scqubits.tests directory
    if not os.path.exists(TEMPDIR):
        os.makedirs(TEMPDIR)
    nose.run(defaultTest="scqubits.tests", argv=['nosetests', '-v', '--nologcapture'])

