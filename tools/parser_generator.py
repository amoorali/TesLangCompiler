from tools.symbol_table import SymbolTable
from tools.ast import AbstractSyntaxTree
from tools.error_generator import Error


class ParserGenerator:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.tokens.reverse()
        self.types = ['_NUMBER', '_LIST', '_NULL']
        [print(item) for item in self.tokens]
        print()

        while self.get_token():
            if self.get_token().name == 'FUNC':
                self.drop_token()
                self.create_func()

            elif self.get_token().name == 'EOF':
                self.drop_token()
                self.drop_token()
                return

            else:
                Error(SyntaxError, 'function', self.get_token().value, self.get_token().line)
                


    def create_func(self):
        """func :=
                FUNC ID ( flist ) : Type => { body }    |
                FUNC ID ( flist ) : Type => expr
        """
        if self.get_token().name == 'ID':
            self.drop_token()
            if self.get_token().name == 'LPAREN':
                self.drop_token()
                self.create_flist()
                if self.get_token().name == 'RPAREN':
                    self.drop_token()
                    if self.get_token().name == 'COLON':
                        self.drop_token()
                        if self.get_token().name in self.types:
                            self.drop_token()
                            if self.get_token().name == 'ARROW':
                                self.drop_token()
                                if self.get_token().name == 'LBRACE':
                                    self.drop_token()
                                    self.create_body()
                                    if self.get_token().name != 'RBRACE':
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
        if self.get_token().name == 'ID':
            self.drop_token()    
            if self.get_token().name == 'COLON':
                self.drop_token()
                if self.get_token().name in self.types:
                    self.drop_token()
                    if self.get_token().name == 'COMMA':
                        self.drop_token()
                        if self.get_token().name != 'ID':
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