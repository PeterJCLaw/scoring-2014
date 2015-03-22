#!/usr/bin/env python

from __future__ import absolute_import

import os
import sys

path = os.path.dirname(os.path.realpath(__file__)) + "/lib/"
sys.path.insert(0, path)

from scorer import Scorer

if __name__ == '__main__':
    path = os.path.join(path, "libproton/")
    sys.path.insert(0, path)

    import libproton

    libproton.main(Scorer)
