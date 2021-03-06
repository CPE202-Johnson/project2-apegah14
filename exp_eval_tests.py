# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        self.assertAlmostEqual(postfix_eval("3 5 - 3 * 2 **"), 36)

    def test_postfix_eval_06(self):
        self.assertAlmostEqual(postfix_eval("3 6 + 3 /"), 3)

    def test_postfix_eval_07(self):
        self.assertRaises(ValueError, postfix_eval, "3 0 /")

    def test_prefix_to_postfix_01(self):
        self.assertEqual(prefix_to_postfix("- 5 - -7.1 - 11 3"), "5 -7.1 11 3 - - -")


if __name__ == "__main__":
    unittest.main()
