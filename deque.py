# Solution ID: 52187518
ERROR_CODE = 'error'


class Deque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push_front(self, value):
        if self.size == self.max_size:
            return ERROR_CODE
        self.head = (self.head - 1) % self.max_size
        self.items[self.head] = value
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            return ERROR_CODE
        value = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    def push_back(self, value):
        if self.size == self.max_size:
            return ERROR_CODE
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            return ERROR_CODE
        self.tail = (self.tail - 1) % self.max_size
        value = self.items[self.tail]
        self.size -= 1
        return value


if __name__ == '__main__':
    command_count = int(input())
    deque = Deque(max_size=int(input()))
    while(command_count):
        command, *argument = input().split(' ')
        if command == 'push_front':
            result = deque.push_front(argument[0])
        elif command == 'push_back':
            result = deque.push_back(argument[0])
        elif command == 'pop_front':
            result = deque.pop_front()
        elif command == 'pop_back':
            result = deque.pop_back()
        if result is not None:
            print(result)
        command_count -= 1
