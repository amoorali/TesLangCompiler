from enum import Enum
from collections import namedtuple
import re


token_info = namedtuple("Tokens", ["name", "value", "line"])

ILLEGAL = 'ILLEGAL'
EOF     = 'EOF'


class Token(Enum):
    # keywords
    FUNC    = re.compile(r'function')
    LET     = re.compile(r'let')
    FOR     = re.compile(r'for')
    WHILE   = re.compile(r'while')
    IF      = re.compile(r'if')
    ELSE    = re.compile(r'else')
    OF      = re.compile(r'of')
    RETURN  = re.compile(r'return')

    # data types
    _NUMBER = re.compile(r'Number')
    _LIST   = re.compile(r'List')
    _NULL   = re.compile(r'Null')

    # identifier
    ID      = re.compile(r'[A-Za-z_][A-Za-z_\d+]*')

    # number
    NUMBER  = re.compile(r'[\d]+')
    
    # comments
    COMMENT = re.compile(r'\/\/.*')
    NEWLINE = re.compile(r'[\n\r]')

    # paranthesis
    LPAREN  = re.compile(r'\(')
    RPAREN  = re.compile(r'\)')

    # bracket
    LSQUARE = re.compile(r'\[')
    RSQUARE = re.compile(r'\]')

    # brace
    LBRACE  = re.compile(r'\{')
    RBRACE  = re.compile(r'\}')

    # punctuators
    SEMICOLON  = re.compile(r';')
    COLON   = re.compile(r':')
    PERIOD  = re.compile(r'\.')
    Q_MARK  = re.compile(r'\?')
    COMMA   = re.compile(r',')
    ARROW   = re.compile(r'\=\>')

    # conditional operators
    LARGE   = re.compile(r'>')
    LARGEEQ = re.compile(r'>\=')
    EQUAL   = re.compile(r'\=\=')
    SMALL   = re.compile(r'<')
    SMALLEQ = re.compile(r'<\=')
    NOTEQ   = re.compile(r'!\=')

    # operators
    ASSIGN  = re.compile(r'\=')

    # athemetic operators
    PLUS    = re.compile(r'\+')
    MINUS   = re.compile(r'\-')
    TIMES   = re.compile(r'\*')
    DIVIDE  = re.compile(r'\/')
    MODULUS = re.compile(r'%')

    # logical operators
    AND     = re.compile(r'&&')
    OR      = re.compile(r'\|\|')
    NOT     = re.compile(r'!')

    # whitespace
    WHITESPACE = re.compile(r'(\t|\s)+')
