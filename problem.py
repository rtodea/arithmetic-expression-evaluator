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

    def __init__(self, operation=None, left=None, right=None, parent=None):
        self.operation = None
        self.left = left
        self.right = None
        self.parent = None


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


def root_of_expression(expression: Expression) -> Expression:
    if expression.parent is None:
        return expression
    parent: Expression = expression.parent
    while parent.parent is not None:
        parent = parent.parent
    return parent


def symbol_to_expression(symbol: str) -> Expression:
    symbol_expression = Expression()
    symbol_expression.left = symbol

    return symbol_expression


def has_higher_order(first: str, second: str) -> bool:
    return first in ['*', '/'] and second in ['+', '-']


def calculate(expression_as_string: str) -> float:
    operations = ['+', '-', '*', '/']
    symbol = ''
    current_expression: Expression = None
    for c in expression_as_string:
        if c in operations:
            symbol_expression = symbol_to_expression(symbol)
            symbol = ''

            if current_expression is None:
                current_expression = Expression()
                current_expression.left = symbol_expression

                current_expression.operation = c
            else:
                new_expression: Expression = Expression()
                new_expression.operation = c

                if has_higher_order(current_expression.operation, c):
                    current_expression.right = symbol_expression
                    new_expression.left = current_expression
                    #
                    current_expression.parent.right = new_expression
                    new_expression.parent = current_expression.parent
                    current_expression.parent = new_expression
                else:
                    new_expression.left = symbol_expression
                    new_expression.parent = current_expression
                    current_expression.right = new_expression
                current_expression = new_expression
        else:
            symbol = symbol + c
    if current_expression is None:
        return 0

    symbol_expression = symbol_to_expression(symbol)
    current_expression.right = symbol_expression

    root = root_of_expression(current_expression)

    return evaluate(root)
