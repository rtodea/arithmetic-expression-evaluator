import unittest

from problem import calculate, Expression, evaluate


class ProblemTestCase(unittest.TestCase):

    def test_expression_element(self):
        expression: Expression = Expression()
        expression.right = Expression(None, '10')
        expression.operation = '+'
        expression.left = Expression(None, '10')

        answer = evaluate(expression)
        self.assertEqual(20, answer)

    def test_simple_expression(self):
        self.assertEqual(20, calculate('10+10'))

    def test_simple_expression_minus(self):
        self.assertEqual(10, calculate('20-10'))

    def test_simple_expression_multiply(self):
        self.assertEqual(100, calculate('10*10'))

    def test_simple_expression_divide(self):
        self.assertEqual(1, calculate('10/10'))

    def test_multiple_expressions(self):
        self.assertEqual(22, calculate('10+10+2'))

    def test_multiple_expression_with_precedence(self):
        self.assertEqual(30, calculate('10+10*2'))

    def test_multiple_expression_with_two_precedence(self):
        self.assertEqual(35, calculate('10+10*2+5'))


if __name__ == '__main__':
    unittest.main()
