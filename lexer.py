from tools.lexer_generator import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()
    
    def _add_token(self):
        # identifier
        self.lexer.add('identifier', r'[A-Za-z_][A-Za-z_\d+]*')

        # number
        self.lexer.add('number', r'[\d]+')

        # paranthesis
        self.lexer.add('open_paran', r'\(')
        self.lexer.add('close_paran', r'\)')

        # bracket
        self.lexer.add('open_bracket', r'\[')
        self.lexer.add('close_bracket', r'\]')

        # brace
        self.lexer.add('open_brace', r'\{')
        self.lexer.add('close_brace', r'\}')

        # punctuators
        self.lexer.add('semi_colon', r'\;')
        self.lexer.add('colon', r'\:')
        self.lexer.add('period', r'\.')
        self.lexer.add('ques_mark', r'\?')
        self.lexer.add('exclam_point', r'\!')
        self.lexer.add('comma', r'\,')
        self.lexer.add('arrow', r'\=\>')

        # operators
        self.lexer.add('sum', r'\+')
        self.lexer.add('sub', r'\-')
        self.lexer.add('mul', r'\*')
        self.lexer.add('div', r'\/^\/')
        self.lexer.add('mod', r'\%')
        self.lexer.add('assign', r'\=^\=')

        # comparison operators
        self.lexer.add('greater', r'\>')
        self.lexer.add('lesser', r'\<')
        self.lexer.add('equal', r'\=\=')
        self.lexer.add('greater_equal', r'\>\=')
        self.lexer.add('lesser_equal', r'\<\=')
        self.lexer.add('not_equal', r'\!\=')

        # logical operators
        self.lexer.add('and', r'\&\&')
        self.lexer.add('or', r'\|\|')

        # comment
        self.lexer.add('comment', r'\/\/.*')

    def get_lexer(self):
        self._add_token()
        return self.lexer.build()
