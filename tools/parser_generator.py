from tools.symbol_table import SymbolTable
from tools.ast import AbstractSyntaxTree
from tools.error_generator import Error
from tools.tokens import *


class ParserGenerator:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.tokens.reverse()
        self.types = [Token._NUMBER.name, Token._LIST.name, Token._NULL.name]
        [print(item) for item in self.tokens]
        print()

        while self.get_token():
            if self.get_token().name == Token.FUNC.name:
                self.drop_token()
                self.create_func()

            elif self.get_token().name == EOF:
                self.drop_token()
                self.drop_token()
                return

            else:
                Error(SyntaxError, 'function', self.get_token().value, self.get_token().line)
                


    def create_func(self):
        """`func` :=
                FUNC ID ( `flist` ) : Type => { `body` }    |
                FUNC ID ( `flist` ) : Type => `expr`
        """
        if self.get_token().name == Token.ID.name:
            self.drop_token()
            if self.get_token().name == Token.LPAREN.name:
                self.drop_token()
                self.create_flist()
                if self.get_token().name == Token.RPAREN.name:
                    self.drop_token()
                    if self.get_token().name == Token.COLON.name:
                        self.drop_token()
                        if self.get_token().name in self.types:
                            self.drop_token()
                            if self.get_token().name == Token.ARROW.name:
                                self.drop_token()
                                if self.get_token().name == Token.LBRACE.name:
                                    self.drop_token()
                                    self.create_body()
                                    if self.get_token().name != Token.RBRACE.name:
                                        Error(SyntaxError, '}', self.get_token().value, self.get_token().line).raise_error()
                                else:
                                    self.create_expr()

                            else:
                                Error(SyntaxError, '=>', self.get_token().value, self.get_token().line).raise_error()
                        else:
                            Error(SyntaxError, 'an expression type', self.get_token().value, self.get_token().line).raise_error()
                    else:
                        Error(SyntaxError, ':', self.get_token().value, self.get_token().line).raise_error()
                else:
                    Error(SyntaxError, ')', self.get_token().value, self.get_token().line).raise_error()
            else:
                Error(SyntaxError, '(', self.get_token().value, self.get_token().line).raise_error()
        else:
            Error(SyntaxError, 'function name', self.get_token().value, self.get_token().line).raise_error()

    def create_flist(self):
        """flist :=
                                    |
                ID : Type           |
                ID : Type , flist
        """
        if self.get_token().name == Token.ID.name:
            self.drop_token()    
            if self.get_token().name == Token.COLON.name:
                self.drop_token()
                if self.get_token().name in self.types:
                    self.drop_token()
                    if self.get_token().name == Token.COMMA.name:
                        self.drop_token()
                        if self.get_token().name != Token.ID.name:
                            Error(SyntaxError, 'an argument', self.get_token().value, self.get_token().line).raise_error()
                        else:
                            self.create_flist()
                    else:
                        return
                else:
                    Error(SyntaxError, 'an expression type', self.get_token().value, self.get_token().line).raise_error()    
            else:
                Error(SyntaxError, ':', self.get_token().value, self.get_token().line).raise_error()
        return

    def create_body(self):
        pass

    def create_expr(self):
        pass
        
    def drop_token(self):
        print(self.tokens.pop())

    def get_token(self):
        return self.tokens[-1]