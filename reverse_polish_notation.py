# Solution ID: 52211296
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
        except IndexError as error:
            raise RuntimeError(error)


def reverse_polish_calculate(operands, stack=Stack(), digitizer=int,
                             operators=OPERATORS):
    for argument in operands:
        if argument in operators:
            right, left = stack.pop(), stack.pop()
            new_value = operators[argument](left, right)
        else:
            try:
                new_value = digitizer(argument)
            except ValueError:
                raise ValueError(ERROR_DIGITIZE.format(argument=argument))
        stack.push(new_value)
    return stack.pop()


if __name__ == '__main__':
    print(reverse_polish_calculate(input().split(' ')))
