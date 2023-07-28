class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None # type: ignore

class StackLinkedList:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top
    
    def push(self, value: int):
        node = Node(value)
        if self.length == 0:
            self.top = node
            self.bottom = node
        else:
            node.next = self.top
            self.top = node

        self.length += 1
        return self
    
    def pop(self):
        top = self.top
        if self.length == 0:
            return self
        if self.length == 1:
            self.top = None
            self.bottom = None
        else:
            self.top = self.top.next
        self.length -= 1
        return top
    
    def print_stack(self) -> list:
        array = []
        current = self.top
        while current != None:
            array.append(current.value)
            current = current.next
        return array
    
    def is_empty(self) -> bool:
        return self.length == 0
    
class StackArray:
    def __init__(self) -> None:
        self.data = []
    
    def peek(self):
        return self.data[len(self.data) - 1]
    
    def push(self, value):
        self.data.append(value)
        return self
    
    def pop(self):
        return self.data.pop()
    
    def print_stack(self) -> list:
        return self.data
    
    def is_empty(self) -> bool:
        return len(self.data) == 0