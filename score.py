#!/usr/bin/env python

import os
import sys

path = os.path.dirname(os.path.realpath(__file__)) + "/lib/"
sys.path.insert(0, path)

from scorer import Scorer

def score(teams_data):
    return Scorer(teams_data).calculate_scores()

if __name__ == '__main__':
    path = os.path.join(path, "libproton/")
    sys.path.insert(0, path)

    import libproton

    libproton.main(score)
