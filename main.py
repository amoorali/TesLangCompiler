from tools.lexer import Lexer
from tools.parser_generator import ParserGenerator
from tools.number_op import *
from nodes import *


txt = ""
with open('Tests/test1.txt', 'r') as input_file:
    for line in input_file.readlines():
        txt += line

lexer = list(Lexer(txt))

with open('Tests/myAns1.txt', 'w') as out:
    for item in lexer:    
        out.write(item.value + '\n')

parser = ParserGenerator(lexer)

# for item in lexer:
#     print(item)
#     literal = Literals(item, item.name, item.value)
#     if literal.eval() is not None:
#         print(literal.eval())
#     if item.name == 'ILLEGAL':
#         print('   {}\n   ^\nSyntaxError:\n\tInvalid Syntax at line: {}'.format(item.value, item.line))