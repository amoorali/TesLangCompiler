from tools.lexer import Lexer
from tools.parser_generator import ParserGenerator
from tools.number_op import *
from nodes import *


txt = """function count_even_numbers(A): Number => { // salam
    let even_count: Number = 0;

    for (i, v of A) {
        if (v % 2 == 0) {
            even_count= even_count + 1;
            even_count = 4 / 3
        }
    }

    return even_count;
}"""

lexer = list(Lexer(txt))
parser = ParserGenerator(lexer)

# for item in lexer:
#     print(item)
#     literal = Literals(item, item.name, item.value)
#     if literal.eval() is not None:
#         print(literal.eval())
#     if item.name == 'ILLEGAL':
#         print('   {}\n   ^\nSyntaxError:\n\tInvalid Syntax at line: {}'.format(item.value, item.line))