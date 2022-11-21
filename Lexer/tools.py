import re

class Token():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return 'Token(\'{}\': \'{}\')'.format(self.name.upper(), self.value)


class LexerGenerator():
    def __init__(self):
        self.tokens = {}
        self.patterns = ''
    
    def add(self, key: str, value: str):
        self.tokens[key] = value

    def lex(self, code_string: str) -> list[Token]:
        tks = re.finditer(self.patterns, code_string)
        result = []
        for match in tks:
            temp = match.group()
            for token, regex in list(self.tokens.items()):
                if re.fullmatch(regex, temp) is not None:
                   result.append(Token(token, temp)) 
        return result


    def build(self):
        self.patterns = "|".join(self.tokens.values())
        self.patterns = '(' + self.patterns + ')'
        return self

