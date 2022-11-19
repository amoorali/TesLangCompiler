import re


IDENTIFIER = r'[A-Za-z_][A-Za-z_\d+]*'
NUMBER = r'[\d]+'
COMMENT = r'(\/\/)(.*?)[\n\r]'
PARAN = r'[{(\[\])}]'
OPERATOR = r'[*-+=<>/%]+'
PONCTUATOR = r'[:;,]'
TOKENS = r'({}|{}|{}|{}|{})'.format(IDENTIFIER, NUMBER, PARAN, OPERATOR, PONCTUATOR)

def getTokens(code_string: str) -> list:
    tk = re.findall(TOKENS, code_string)
    return "\n".join(tk)