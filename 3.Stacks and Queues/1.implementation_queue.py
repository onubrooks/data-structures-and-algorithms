class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


class QueueLinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.value
    
    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        
        self.length += 1
        return self
    
    def dequeue(self):
        if self.length == 0:
            return self
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            tmp = self.first
            self.first = self.first.next
            
        self.length -= 1
        return tmp
    