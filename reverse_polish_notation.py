# Solution ID: 52202637
ERROR_STACK_EMPTY = 'stack empty error'
ERROR_DIGITIZE = 'Failure in digitization: {argument}'
OPERATORS = {
    '-': lambda left, right: left - right,
    '+': lambda left, right: left + right,
    '*': lambda left, right: left * right,
    '/': lambda left, right: left // right,
}


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise RuntimeError(ERROR_STACK_EMPTY)


def reverse_polish_calculate(operands, stack=Stack(), digitizer=int,
                             operators=OPERATORS):
    for argument in operands:
        try:
            new_value = digitizer(argument)
        except ValueError:
            if argument not in operators:
                raise ValueError(ERROR_DIGITIZE.format(argument=argument))
            operand_right, operand_left = stack.pop(), stack.pop()
            new_value = operators[argument](operand_left,
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
