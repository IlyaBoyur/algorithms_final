# Solution ID: 52202637
ERROR_STACK_EMPTY = 'stack empty error'
ERROR_INVALID_OPERATOR = 'invalid operator error'
MINUS = '-'
PLUS = '+'
MULTIPLY = '*'
DIVIDE = '/'
OPERATOR_TO_FUNCTION = {
    MINUS: lambda operand_left, operand_right: operand_left - operand_right,
    PLUS: lambda operand_left, operand_right: operand_left + operand_right,
    MULTIPLY: lambda operand_left, operand_right: operand_left * operand_right,
    DIVIDE: lambda operand_left, operand_right: operand_left // operand_right,
}


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
    for argument in operands:
        try:
            new_value = int(argument)
        except ValueError:
            if argument not in OPERATOR_TO_FUNCTION:
                raise ValueError(ERROR_INVALID_OPERATOR)
            operand_right, operand_left = stack.pop(), stack.pop()
            new_value = OPERATOR_TO_FUNCTION[argument](operand_left,
                                                       operand_right)
        stack.push(new_value)
    return stack.pop()


if __name__ == '__main__':
    try:
        print(reverse_polish_calculate(input().split(' ')))
    except ValueError:
        pass
    except RuntimeError:
        pass
