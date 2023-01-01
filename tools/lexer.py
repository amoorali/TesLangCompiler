from tools.tokens import *


def Lexer(code_string: str) -> token_info:
    """Create a generator object containing Tokens of a string

    Args:
        code_string (str): Represents the input code to lex.

    Returns:
        Tokens (namedtuple): A named tuple containing information about tokens of the code
    """
    pos = 0
    line = 1
    while pos < len(code_string):
        for tk in Token:
            if match := tk.value.match(code_string, pos):
                pos = match.end(0)
                if tk == Token.NEWLINE:
                    line += 1
                    break
                if tk == Token.WHITESPACE or tk == Token.COMMENT:
                    # ignore white spaces and comments
                    break
                yield token_info(tk.name, match.group(0), line)
                break
        else:
            # in case pattern doesn't match send the charector as illegal
            yield token_info(ILLEGAL, code_string[pos], line)
            pos += 1
    else:
        # in parser we read the token two times each iteration
        # once for current token and one for next token
        # so handing it by sending EOF 2 times
        yield token_info(EOF, '\x00', line)
        yield token_info(EOF, '\x00', line)

class LexerGenerator:
    def __init__(self, file_path) -> None:
        self._file_path = file_path
        self._pointer = 0
        self._line = 1
        self.next_token = self.get_token()
        

    def get_token(self):
        token = ''
        with open(self._file_path, 'r') as file:
            temp_result = None
            file.seek(self._pointer)
            while True:
                char = file.read(1)
                self._pointer += 1
                
                temp_tk = token + char

                for tk in Token:
                    if tk.value.match(temp_tk):
                        # print(f'-{temp_tk}-', '\t\t', self._pointer)
                        if tk == Token.NEWLINE:
                            self._line += 1
                            self._pointer += 1
                            temp_tk = ''
                            break
                        if tk == Token.COMMENT:
                            while True:
                                char = file.read(1)
                                self._pointer += 1
                                if Token.NEWLINE.value.match(char):
                                    self._line += 1
                                    break
                            temp_tk = ''
                        elif tk == Token.WHITESPACE:
                            # ignore white spaces
                            break

                        token = temp_tk
                        temp_result = token_info(tk.name, token, self._line)
                        break
                else:
                    # in case pattern doesn't match send the charector as illegal
                    if temp_result == None:
                        return token_info(ILLEGAL, temp_tk, self._line)

                    return temp_result

    def drop_token(self):
        self.next_token = self.get_token()
