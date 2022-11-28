import re
from tools.token_struct import Token

class LexerGenerator():
    def __init__(self):
        self.tokens = {}
        self.patterns = ''
    
    def add(self, key: str, value: str):
        """Add a token to the lexer.

        Args:
            key (str): Name of the token
            value (str): RegEx of the token
        """
        
        self.tokens[key] = value

    def lex(self, code_string: str) -> list[Token]:
        """Generate a list of tokens from the argument.

        Args:
            code_string (str): Represents the input code to lex.

        Returns:
            list[Token]: A list containing tokens of the code
        """

        tks = re.finditer(self.patterns, code_string) # find all tokens by patterns
        result = []

        # for every token in our list, try to match each token with the tokens
        # added to our lexer to extract the name and the type of the token
        for tk in tks:
            temp = tk.group()
            print(temp)
            for token, regex in list(self.tokens.items()):
                if re.fullmatch(regex, temp) is not None:
                   result.append(Token(token, temp))
                   break
        return result


    def build(self):
        self.patterns = "|".join(self.tokens.values())
        self.patterns = '(' + self.patterns + ')'
        return self

