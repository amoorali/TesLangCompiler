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
