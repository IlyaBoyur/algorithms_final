# Solution ID: 52211312
ERROR_CODE = 'error'
ERROR_INVALID_COMMAND = 'Unsupported command: {command}'


class Deque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 1
        self.tail = 0
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push_front(self, value):
        if self.size == self.max_size:
            raise RuntimeError(ERROR_CODE)
        self.head = (self.head - 1) % self.max_size
        self.items[self.head] = value
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise RuntimeError(ERROR_CODE)
        value = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    def push_back(self, value):
        if self.size == self.max_size:
            raise RuntimeError(ERROR_CODE)
        self.tail = (self.tail + 1) % self.max_size
        self.items[self.tail] = value
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise RuntimeError(ERROR_CODE)
        value = self.items[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return value


if __name__ == '__main__':
    command_count = int(input())
    deque = Deque(max_size=int(input()))
    for _ in range(command_count):
        try:
            command, *arguments = input().split(' ')
            result = getattr(deque, command)(*arguments)
            if 'pop' in command:
                print(result)
        except RuntimeError as error:
            print(error)
        except AttributeError:
            raise ValueError(ERROR_INVALID_COMMAND.format(command=command))
