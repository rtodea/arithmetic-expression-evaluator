# input: 10+5*2
# output: 20
#
# operations: +, -, *, /
#
# int
# 10+5 => expression(operation, operands)
# operation: +
# operands: 10, 5
#
# tree
# [+]
# |  \
# 10  10

# 1
# symbol = 1
# 10
# symbol = 10
# 10+
# expression(+, 10, ?)
#
# 10+1
#

# 10+10+2
# 10+10
# new_expression(+, 10)
# symbol = 10
# 10+10+
#


# Express
# left
# Expression


class Expression:

    # def __init__(self):
    # self.left = left
    # self.operation = operation
    # self.right = right

    def __init__(self):
        self.operation = None
        self.left = None
        self.right = None

    # def evaluate(self):
    #     if self.operation == '+':
    #         return self.left + self.right
    #     if self.operation == '-':
    #         return self.left - self.right
    #     if self.operation == '*':
    #         return self.left * self.right
    #     if self.operation == '/':
    #         return self.left / self.right


def evaluate(e: Expression) -> float:
    if e.operation is None and e.right is None:
        return int(e.left)

    if e.operation == '+':
        return evaluate(e.left) + evaluate(e.right)
    if e.operation == '-':
        return evaluate(e.left) - evaluate(e.right)
    if e.operation == '*':
        return evaluate(e.left) * evaluate(e.right)
    if e.operation == '/':
        return evaluate(e.left) / evaluate(e.right)


def calculate(expression_as_string: str) -> float:
    operations = ['+', '-', '*', '/']
    symbol = ''
    current_expression = None
    for c in expression_as_string:
        if c in operations:
            if current_expression is None:
                symbol_expression = Expression()
                symbol_expression.left = symbol
                symbol = ''

                current_expression = Expression()
                current_expression.left = symbol_expression

                current_expression.operation = c
            else:
                symbol_expression = Expression()
                symbol_expression.left = symbol
                symbol = ''

                current_expression.right = symbol_expression
                new_expression = Expression()
                new_expression.left = current_expression
                new_expression.operation = c

                current_expression = new_expression
        else:
            symbol = symbol + c
    if current_expression is None:
        return 0

    symbol_expression = Expression()
    symbol_expression.left = symbol

    current_expression.right = symbol_expression

    return evaluate(current_expression)
