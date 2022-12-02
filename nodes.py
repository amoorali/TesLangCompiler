from tools.tokens import *

class Node:
    pass

class Expression:
    pass

class Statement:
    pass

class Literals(Expression):
    def __init__(self, token: token_info, type: str, value: str) -> None:
        self.token = token
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)

    def type_cast(self):
        if self.type == Token.NUMBER.name:
            return int(self.value)
    
    def eval(self):
        try:
            out = self.type_cast()
        except ValueError:
            raise(f'Error converting {self.value} to {self.type}')
        
        return out