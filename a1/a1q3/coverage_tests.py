import unittest

from .token_with_escape import token_with_escape
from .token_with_escape_mutant1 import token_with_escape_mutant1
from .token_with_escape_mutant2 import token_with_escape_mutant2

class CoverageTests(unittest.TestCase):
    def test_statement_coverage(self):
        """Add tests to achieve statement coverage (as many as needed)."""
        #self.assertEqual(token_with_escape('one^|uno||three^^^^|four^^^|^cuatro|'),['one|uno', '', 'three^^', 'four^|cuatro',''])
        self.assertEqual(token_with_escape('^abc|def|'),
                         ['abc', 'def', ''])
        pass

    def test_kill_mutant_1(self):
        """Kill mutant 1"""
        # YOUR CODE HERE
        #self.assertEqual(token_with_escape_mutant1('^abc|def|'),
        #                 ['abc', 'def', ''])
        self.assertEqual(token_with_escape_mutant1('one^|uno||three^^^^|four^^^|^cuatro|'),
                         ['one|uno', '', 'three^^', 'four^|cuatro', ''])
        pass

    def test_kill_mutant_2(self):
        """Kill mutant 2"""
        # YOUR CODE HERE
        #self.assertEqual(token_with_escape_mutant2('^abc|def|'),
        #                 ['abc', 'def', ''])
        self.assertEqual(token_with_escape_mutant2('one^|uno||three^^^^|four^^^|^cuatro|'),
                         ['one|uno', '', 'three^^', 'four^|cuatro', ''])
        pass
