from tools.lexer import Lexer
from tools.parser_generator import ParserGenerator
from tools.number_op import *
from nodes import *

# tks = []
# lg = LexerGenerator(file_path='Tests/test1.txt')
# for _ in range(102):
#     print(lg.next_token)
#     lg.drop_token()


txt = ''
with open('Tests/test1.txt', 'r') as file:
    for line in file.readlines():
        txt += line

lexer = list(Lexer(txt))
for item in lexer:
    print(item)

# with open('Tests/myAns1.txt', 'w') as out:
#     for item in lexer:    
#         out.write(item.value + '\n')

parser = ParserGenerator(lexer)

