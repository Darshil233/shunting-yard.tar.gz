class ExpressionEvaluator:
    def __init__(self, invert_precedence=False):
        self.invert_precedence = invert_precedence
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        if self.invert_precedence:
            self.precedence = {k: -v for k, v in self.precedence.items()}

    def parse(self, expression):
        output = []
        operators = Stack()
        tokens = expression.split()

        for token in tokens:
            if token.isnumeric():
                output.append(token)
            elif token == '(':
                operators.push(token)
            elif token == ')':
                while operators and operators.peek() != '(':
                    output.append(operators.pop())
                operators.pop()
            else:
                while (operators and operators.peek() in self.precedence and
                       self.precedence[token] <= self.precedence[operators.peek()]):
                    output.append(operators.pop())
                operators.push(token)

        while operators:
            output.append(operators.pop())

        return ' '.join(output)

    def evaluate(self, expression):
        operands = Stack()
        tokens = expression.split()

        for token in tokens:
            if token.isnumeric():
                operands.push(int(token))
            else:
                right = operands.pop()
                left = operands.pop()
                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                elif token == '/':
                    result = left / right
                operands.push(result)

        return operands.pop()
