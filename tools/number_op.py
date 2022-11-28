class Number:
    def __init__(self, value) -> None:
        self.value = value

    def eval(self):
        return self.value


class BinaryOp:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left + self.right


class Sub(BinaryOp):
    def eval(self):
        return self.left - self.right


class Mul(BinaryOp):
    def eval(self):
        return self.left * self.right


class Div(BinaryOp):
    def eval(self):
        return self.left / self.right