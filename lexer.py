import re

IDENTIFIER = r'[A-Za-z_][A-Za-z_0-9]*'
NUMBER = r'[0-9]+'
COMMENT = r'(\/\/)(.*?)[\n\r]'


def getTokens(code_string: str) -> list:
    # re.search(r'[]')
    pass