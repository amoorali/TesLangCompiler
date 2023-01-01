from tools.lexer import *
from tools.parser_generator import ParserGenerator
from tools.number_op import *
from nodes import *

tks = []
lg = LexerGenerator(file_path='Tests/test1.txt')
for _ in range(20):
    print(lg.next_token)
    lg.drop_token()




# lexer = list(Lexer(txt))

# with open('Tests/myAns1.txt', 'w') as out:
#     for item in lexer:    
#         out.write(item.value + '\n')

# parser = ParserGenerator(lexer)

# for item in lexer:
#     print(item)
#     literal = Literals(item, item.name, item.value)
#     if literal.eval() is not None:
#         print(literal.eval())
#     if item.name == 'ILLEGAL':
#         print('   {}\n   ^\nSyntaxError:\n\tInvalid Syntax at line: {}'.format(item.value, item.line))