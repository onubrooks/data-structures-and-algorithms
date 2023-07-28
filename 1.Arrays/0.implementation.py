"""
This is a very simple and basic implementation of an array.
"""
class Array:
    def __init__(self, size):
        self.size = size
        self.data = dict()

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.size] = item
        self.size += 1
        return self.size

    def pop(self):
        last_item = self.data[self.size - 1]
        del self.data[self.size - 1]
        self.size -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self.shift(index)
        return item

    def shift(self, index):
        for i in range(index, len(self.data) - 1):
            self.data[i] = self.data[i + 1]
        del self.data[len(self.data) - 1]
        self.size -= 1

    def unshift(self, index):
        for i in range(len(self.data), index, -1):
            self.data[i] = self.data[i - 1]
        self.size -= 1

    def insert(self, index, item):
        self.unshift(index)
        self.data[index] = item
        self.size += 1