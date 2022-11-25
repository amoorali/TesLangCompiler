import unittest
from lexer import Lexer

input_code = ""
with open('Tests/test1.txt', 'r') as test_file:
    for line in test_file:
        input_code += line

output = ""
with open('Tests/test1_answer.txt', 'r') as answer_file:
    for line in answer_file:
        output += line


class TestLexer(unittest.TestCase):
    def runTest(self):
        self.maxDiff = None
        lexer = Lexer().get_lexer()
        self.assertEqual(lexer.lex(input_code), output, "wrong output!")


unittest.main()