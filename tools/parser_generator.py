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
            if self.is_token(Token.FUNC):
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
        1       FUNC ID ( `flist` ) : Type => { `body` }    |
        2       FUNC ID ( `flist` ) : Type => `expr`
        """
        if self.is_token(Token.ID):
            self.drop_token()
            if self.is_token(Token.LPAREN):
                self.drop_token()
                self.create_flist()
                if self.is_token(Token.RPAREN):
                    self.drop_token()
                    if self.is_token(Token.COLON):
                        self.drop_token()
                        if self.get_token().name in self.types:
                            self.drop_token()
                            if self.is_token(Token.ARROW):
                                self.drop_token()
                                if self.is_token(Token.LBRACE):
                                    self.drop_token()
                                    self.create_body()
                                    if self.get_token().name != Token.RBRACE.name:
                                        Error(SyntaxError, '}', self.get_token().value, self.get_token().line).raise_error()
                                    else:
                                        self.drop_token()
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
        """`flist` :=
        1                           |
        2       ID : Type           |
        3       ID : Type , `flist`
        """
        if self.is_token(Token.ID):
            self.drop_token()    
            if self.is_token(Token.COLON):
                self.drop_token()
                if self.get_token().name in self.types:
                    self.drop_token()
                    if self.is_token(Token.COMMA):
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
        """`body` :=
        1                     |
        2       `stmt` `body`
        """
        if self.is_token(Token.RBRACE):
            return
        self.create_stmt()

    def create_stmt(self):
        """`stmt` :=
        1       `expr`;                                     |
        2       `defvar`;                                   |
        3       if ( `expr` ) { `stmt` }                    |
        4       if ( `expr` ) { `stmt` } else { `stmt` }    |
        5       while ( expr ) { `stmt` }                   |
        6       for (ID , ID of `expr`) `stmt`              |
        7       return `expr`;                              |
        8       { `body` }                                  |
        9       `func`
        """
        def open_paren():
            if self.is_token(Token.LPAREN):
                self.drop_token()
                return True
            
            Error(SyntaxError, '(', self.get_token().value, self.get_token().line).raise_error()
            return False

        def close_paren():
            if self.is_token(Token.RPAREN):
                self.drop_token()
                return True
            
            Error(SyntaxError, ')', self.get_token().value, self.get_token().line).raise_error()
            return False


        def open_brace():
            if self.is_token(Token.LBRACE):
                self.drop_token()
                return True

            Error(SyntaxError, '{', self.get_token().value, self.get_token().line).raise_error()
            return False
                    
        def close_brace():


            Error(SyntaxError, '}', self.get_token().value, self.get_token().line).raise_error()
            return False

        def semi_colon():
            if self.is_token(Token.SEMICOLON):
                self.drop_token()
                return True
            
            Error(SyntaxError, ';', self.get_token().value, self.get_token().line).raise_error()
            return False

        def defvar_stmt():
            """defvar :=
            1       let ID : Type           |
            2       let ID : Type = expr
            """
            if self.is_token(Token.LET):
                self.drop_token()
                if self.is_token(Token.ID):
                    self.drop_token()
                    if self.is_token(Token.COLON):
                        self.drop_token()
                        if self.get_token().name in self.types:
                            self.drop_token()
                            if self.is_token(Token.ASSIGN):
                                self.drop_token()
                                self.create_expr()
                        else:
                            Error(SyntaxError, 'an expression type', self.get_token().value, self.get_token().line).raise_error()
                    else:
                        Error(SyntaxError, ':', self.get_token().value, self.get_token().line).raise_error()
                else:
                    Error(SyntaxError, 'variable name', self.get_token().value, self.get_token().line).raise_error()
            return

        def if_stmt():
            self.drop_token()
            if open_paren():
                self.create_expr()
                if close_paren() and open_brace():
                    self.create_stmt()
                    if close_brace():
                        if self.is_token(Token.ELSE):
                            self.drop_token()
                            if open_brace():
                                self.create_stmt()
                                close_brace()
                                
        def while_stmt():
            self.drop_token()
            if open_paren():
                self.create_expr()
                if close_paren() and open_brace():
                    self.create_stmt()
                    close_brace()

        def for_stmt():
            self.drop_token()
            if open_paren():
                if self.is_token(Token.ID):
                    self.drop_token()
                    if self.is_token(Token.COMMA):
                        self.drop_token()
                        if self.is_token(Token.ID):
                            self.drop_token()
                            if self.is_token(Token.OF):
                                self.drop_token()
                                self.create_expr()
                                if close_paren() and open_brace():
                                    self.create_stmt()
                                    close_brace()
                            else:
                                Error(SyntaxError, 'of', self.get_token().value, self.get_token().line).raise_error()
                        else:
                            Error(SyntaxError, 'identifier', self.get_token().value, self.get_token().line).raise_error()
                    else:
                        Error(SyntaxError, ',', self.get_token().value, self.get_token().line).raise_error()
                else:
                    Error(SyntaxError, 'identifier', self.get_token().value, self.get_token().line).raise_error()

        def return_stmt():
            self.drop_token()
            self.create_expr()

        # defvar
        if self.is_token(Token.LET):
            defvar_stmt()
            semi_colon()
        
        # if / if-else
        elif self.is_token(Token.IF):
            if_stmt()
        
        # while
        elif self.is_token(Token.WHILE):
            while_stmt()

        # for    
        elif self.is_token(Token.FOR):
            for_stmt()

        # return
        elif self.is_token(Token.RETURN):
            return_stmt()
            semi_colon()
        
        # new block -> { body }
        elif open_brace():
            self.create_body()
            close_brace()
        
        # func
        elif self.is_token(Token.FUNC):
            self.drop_token()
            self.create_func()

        else:
            self.create_expr()
            semi_colon()

    def create_expr(self):
        """`expr` :=
        1       `expr` [ `expr` ]               |
        2       [ `clist` ]                     |
        3       `expr` ? `expr` : `expr`        |
        4       `expr` + `expr`                 |
        5       `expr` - `expr`                 |
        6       `expr` * `expr`                 |
        7       `expr` / `expr`                 |
        8       `expr` % `expr`                 |
        9       `expr` > `expr`                 |
        10      `expr` < `expr`                 |
        11      `expr` == `expr`                |
        12      `expr` >= `expr`                |
        13      `expr` <= `expr`                |
        14      `expr` != `expr`                |
        15      `expr` || `expr`                |
        16      `expr` && `expr`                |
        17      ! `expr`                        |
        18      + `expr`                        |
        19      - `expr`                        |
        20      `iden`                          |
        21      `iden` = `expr`                 |
        22      `iden` ( `clist` )              |
        23      `number`
        """
        pass

    def create_clist(self):
        """`clist` :=
        1                           |
        2       `expr`              |
        3       `expr` , `clist`    |
        """
        

    def is_token(self, tk):
        return self.get_token().name == tk.name
        
    def drop_token(self):
        print(self.tokens.pop())

    def get_token(self):
        return self.tokens[-1]