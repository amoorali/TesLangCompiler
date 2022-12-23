from tools.symbol_table import SymbolTable
from tools.ast import AbstractSyntaxTree


class ParserGenerator:
    def __init__(self, tokens) -> None:
        self.tokens = tokens.reverse()

        while self.get_token():
            if self.get_token().name == 'FUNC':
                self.drop_token()
                self.create_func()

            elif self.get_token().name == 'EOF':
                self.drop_token()
                self.drop_token()
                return

            else:
                raise ValueError('Syntax Error at line: {}'.format(self.get_token().line))
                


    def create_func(self):
        if self.get_token().name == 'ID':
            self.drop_token()
            if self.get_token().name == 'LPAREN':
                self.drop_token()
                self.create_flist()

        else:
            raise ValueError(f'Syntax Error at line: {self.get_token().line}\n\
            Expected function name but got: `{self.get_token().value}`')

    def create_flist(self):
        if self.get_token().name == 'RPAREN':
            self.drop_token()
        
        elif self.get_token().name == 'ID':
            self.create_arg()
        
        else:
            raise SyntaxError(f'Syntax Error at line: {self.get_token().line}\n\
                Expected argument but got: `{self.get_token().value}`')

    def create_arg(self):
        tks = self.tokens[-2:]
        if tks[-1].name == 'COLON' and tks[-2].name in ['_NUMBER', '_LIST', '_NULL']:
            self.drop_token()
            self.drop_token()
            if self.get_token().name == 'COMMA':
                self.create_flist()
        else:
            raise SyntaxError(f'Syntax Error at line: {self.get_token().line}\n\
                Expected ID:TYPE but got: `{self.get_token().value}{tks[-1].value}{tks[-2].value}`')
        

    def drop_token(self):
        self.tokens.pop()

    def get_token(self):
        return self.tokens[-1]