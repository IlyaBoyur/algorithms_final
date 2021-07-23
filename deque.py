# Solution ID: 52203117
ERROR_CODE = 'error'


class Deque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = -1
        # self.size = 0

    def get_size(self):
        if self.is_empty():
            return 0
        return (self.tail - self.head) % self.max_size + 1

    def is_empty(self):
        # return self.size == 0
        return self.tail == -1

    def push_front(self, value):
        if self.get_size() == self.max_size:
            raise RuntimeError(ERROR_CODE)
        if self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.head = (self.head - 1) % self.max_size
        self.items[self.head] = value
        # self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise RuntimeError(ERROR_CODE)
        value = self.items[self.head]
        if self.head == self.tail:
            self.head = 0
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.max_size
        # self.size -= 1
        return value

    def push_back(self, value):
        if self.get_size() == self.max_size:
            raise RuntimeError(ERROR_CODE)
        self.tail = (self.tail + 1) % self.max_size
        self.items[self.tail] = value
        # self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise RuntimeError(ERROR_CODE)
        value = self.items[self.tail]
        if self.head == self.tail:
            self.head = 0
            self.tail = -1
        else:
            self.tail = (self.tail - 1) % self.max_size
        # self.size -= 1
        return value


if __name__ == '__main__':
    command_count = int(input())
    deque = Deque(max_size=int(input()))
    for _ in range(command_count):
        try:
            command, *arguments = input().split(' ')
            result = getattr(deque, command)(*arguments)
            if result is not None:
                print(result)
        except RuntimeError as error:
            print(error)
        except AttributeError as error:
            print(error)
