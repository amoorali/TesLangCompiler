from token import Token


class Lexer():
    def __init__(self):
        self.lexer = r''
        self.tokens = {}
    
    def _add_token(self):
        # identifier
        self.add('identifier', r'[A-Za-z_][A-Za-z_\d+]*')

        # number
        self.add('number', r'[\d]+')

        # paranthesis
        self.add('open_paran', r'\(')
        self.add('close_paran', r'\)')

        # bracket
        self.add('open_bracket', r'\[')
        self.add('close_bracket', r'\]')

        # brace
        self.add('open_brace', r'\{')
        self.add('close_brace', r'\}')

        # punctuators
        self.add('semi_colon', r'\;')
        self.add('colon', r'\:')
        self.add('period', r'\.')
        self.add('ques_mark', r'\?')
        self.add('exclam_point', r'\!')
        self.add('comma', r'\,')
        self.add('arrow', r'\=\>')

        # operators
        self.add('sum', r'\+')
        self.add('sub', r'\-')
        self.add('mul', r'\*')
        self.add('div', r'\/')
        self.add('mod', r'\%')

        # comparison operators
        self.add('greater', r'\>')
        self.add('lesser', r'\<')
        self.add('equal', r'\=\=')
        self.add('greater_equal', r'\>\=')
        self.add('lesser_equal', r'\<\=')
        self.add('not_equal', r'\!\=')

        # logical operators
        self.add('and', r'\&\&')
        self.add('or', r'\|\|')

        # comment
        self.add('comment', r'\/\/.*[\n\r]')

    def add(self, key: str, value: str):
        self.tokens[key] = value

    def _build():
        pass

    def get_lexer(self):
        self._add_token()
        return self._build()
