"""
test.py
=======
written in Python3

author: C. Lockhart <chris@lockhartlab.org>
"""


from izzy.tests import TestGeneric, TestMetrics

import sys
import unittest

test_cases = [
    TestGeneric,
    TestMetrics
]


def test():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for test_case in test_cases:
        suite.addTests(loader.loadTestsFromTestCase(test_case))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    sys.exit(not result.wasSuccessful())


test()
