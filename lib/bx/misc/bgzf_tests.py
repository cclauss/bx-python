from __future__ import print_function

import bx.misc.bgzf
import sys


def test_bgzf():
    f = bx.misc.bgzf.BGZFFile("test_data/bgzf_tests/test.txt.gz", "r")
    assert f.read(10) == b"begin 644 "
    f.seek(0)
    assert f.read(10) == b"begin 644 "
