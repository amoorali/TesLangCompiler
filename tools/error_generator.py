class Error:
    def __init__(self, error, expected_arg, current_arg, line) -> None:
        self.error = error
        self.expected_arg = expected_arg
        self.current_arg = current_arg
        self.line = line

    def __repr__(self) -> str:
        return self.raise_error()

    def raise_error(self):
        if self.error == SyntaxError:
            print(SyntaxError(f'Syntax Error at line: {self.line}\n\
                Expected `{self.expected_arg}` but got: `{self.current_arg}`'))

        elif self.error == ValueError:
            print(ValueError(f'Value Error at line: {self.line}\n\
                Expected `{self.expected_arg}` but got: `{self.current_arg}`'))