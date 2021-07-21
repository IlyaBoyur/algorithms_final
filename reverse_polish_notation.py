# Solution ID: 52187536
ERROR_INDEX = 'index error'
ERROR_ZERO_DIVISION = 'zero division error'
MINUS = '-'
PLUS = '+'
MULTIPLY = '*'
DIVIDE = '/'


class PolishNotationCalculator:
    def __init__(self) -> None:
        self.items = [None]

    def calculate(self, operands):
        try:
            for argument in operands:
                if argument.lstrip(MINUS).isdigit():
                    self.push(int(argument))
                elif argument == PLUS:
                    self.push(self.pop() + self.pop())
                elif argument == MULTIPLY:
                    self.push(self.pop() * self.pop())
                elif argument == MINUS:
                    subtrahend = self.pop()
                    self.push(self.pop() - subtrahend)
                elif argument == DIVIDE:
                    divider = self.pop()
                    self.push(self.pop() // divider)
        except IndexError:
            return ERROR_INDEX
        except ZeroDivisionError:
            return ERROR_ZERO_DIVISION
        return self.pop()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


if __name__ == '__main__':
    calculator = PolishNotationCalculator()
    print(calculator.calculate(input().split(' ')))
