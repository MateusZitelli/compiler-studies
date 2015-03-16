#!/usr/bin/env python

import unittest
import parser


class UtilsTests(unittest.TestCase):
    def test_getTerm(self):
        self.assertEqual(parser.getTerm(parser.T_MINUS),
                         (parser.TERM, parser.T_MINUS))

    def test_getRule(self):
        self.assertEqual(parser.getRule(parser.R_OP),
                         (parser.RULE, parser.R_OP))


class LexicalTests(unittest.TestCase):
    def test_tokenizer(self):
        tokens = parser.lexicalanalysis('(+ 3 (- 2 5))')
        self.assertEqual(tokens, [0, 2, 6, 0, 3, 6, 6, 1, 1, 7])


class SyntaticalTests(unittest.TestCase):
    def test_validation(self):
        testCases = [
            {
                "program": '(+ 3 (-2 4))',
                "expected": True
            },
            {
                "program": '(+ (* 6 (/ 7 8)) (+ 6 7))',
                "expected": True
            },
            {
                "program": '3',
                "expected": True
            },
            {
                "program": '(3 5)',
                "expected": False
            },
            {
                "program": '(* (/ 2 3) (- 2 (+ 4 3)))',
                "expected": True
            },
        ]
        expectedValidations = map(lambda t: t['expected'], testCases)

        programsTokens = map(
            lambda t: parser.lexicalanalysis(t['program']), testCases)
        validationsList = map(parser.syntaticalanalysis, programsTokens)

        for i, tests in enumerate(zip(validationsList, expectedValidations)):
            msg = "In test %i -> %s" % (i, testCases[i]['program'])
            self.assertEqual(tests[0], tests[1], msg=msg)

if __name__ == "__main__":
    unittest.main()
