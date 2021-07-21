# Solution ID: 52187536
ERROR_STACK_EMPTY = 'stack empty error'
ERROR_INVALID_INPUT = 'invalid input error'
ERROR_ZERO_DIVISION = 'zero division error'
MINUS = '-'
PLUS = '+'
MULTIPLY = '*'
DIVIDE = '/'


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise RuntimeError(ERROR_STACK_EMPTY)
        return self.items.pop()


def reverse_polish_calculate(operands):
    stack = Stack()
    try:
        for argument in operands:
            if argument.lstrip(MINUS).isdigit():
                stack.push(int(argument))
            elif argument == PLUS:
                stack.push(stack.pop() + stack.pop())
            elif argument == MULTIPLY:
                stack.push(stack.pop() * stack.pop())
            elif argument == MINUS:
                subtrahend = stack.pop()
                stack.push(stack.pop() - subtrahend)
            elif argument == DIVIDE:
                divider = stack.pop()
                stack.push(stack.pop() // divider)
            else:
                return ERROR_INVALID_INPUT
    except ZeroDivisionError:
        return ERROR_ZERO_DIVISION
    return stack.pop()


if __name__ == '__main__':
    try:
        print(reverse_polish_calculate(input().split(' ')))
    except RuntimeError:
        pass
