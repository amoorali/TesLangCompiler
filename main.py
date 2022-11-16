import unittest, lexer

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
        self.assertEqual(lexer.getTokens(input_code), output, "wrong output!")


unittest.main()