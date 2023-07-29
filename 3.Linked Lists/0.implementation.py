class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def print_list(self):
        array = []
        current_node = self.head
        while current_node != None:
            array.append(current_node.value) # type: ignore
            current_node = current_node.next # type: ignore
        return array
    
    def traverse_to_node(self, index):
        counter = 0
        current = self.head
        while counter != index:
            current = current.next # type: ignore
            counter += 1
        return current
    
    def append(self, value):
        node = Node(value)
        self.tail['next'] = node # type: ignore
        self.tail = node
        self.length += 1
        return self
    
    def prepend(self, value):
        node = Node(value)
        node.next = self.head # type: ignore
        self.head = node
        self.length += 1
        return self
    
    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index >= self.length:
            return self.append(value)
        node = Node(value)
        current = self.traverse_to_node(index - 1)
        node.next = current.next # type: ignore
        current.next = node # type: ignore
        self.length += 1
        return self
    
    def remove(self, index):
        if index == 0:
            self.head = self.head.next # type: ignore
            self.length -= 1
            return self
        if index >= self.length:
            return self
        current = self.traverse_to_node(index - 1)
        current.next = current.next.next # type: ignore
        self.length -= 1
        return self
    
    def reverse(self):
        if self.head.next == None: # type: ignore
            return self.head
        first = self.head
        self.tail = self.head # type: ignore
        second = first.next # type: ignore
        while second != None:
            third = second.next
            second.next = first # type: ignore
            first = second
            second = third
        self.head.next = None # type: ignore
        self.head = first
        return self

my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.insert(2, 99)
my_linked_list.insert(20, 88)
my_linked_list.remove(2)
print(my_linked_list.print_list())

class NodeDouble:
    def __init__(self, value):
        self.value = value
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None,
            'prev': None
        }
        self.tail = self.head
        self.length = 1

    def print_list(self):
        array = []
        current_node = self.head
        while current_node != None:
            array.append(current_node.value) # type: ignore
            current_node = current_node.next # type: ignore
        return array
    
    def traverse_to_node(self, index):
        counter = 0
        current = self.head
        while counter != index:
            current = current.next # type: ignore
            counter += 1
        return current
    
    def append(self, value):
        node = Node(value)
        self.tail.next = node # type: ignore
        node.prev = self.tail # type: ignore
        self.tail = node
        self.length += 1
        return self
    
    def prepend(self, value):
        node = Node(value)
        node.next = self.head # type: ignore
        self.head.prev = node # type: ignore
        self.head = node
        self.length += 1
        return self
    
    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index >= self.length:
            return self.append(value)
        node = Node(value)
        current = self.traverse_to_node(index - 1)
        node.next = current.next # type: ignore
        node.prev = current # type: ignore
        node.next.prev = node # type: ignore
        current.next = node # type: ignore
        self.length += 1
        return self
    
    def remove(self, index):
        if index == 0:
            self.head = self.head.next # type: ignore
            self.length -= 1
            return self
        if index >= self.length:
            return self
        current = self.traverse_to_node(index - 1)
        current.next = current.next.next # type: ignore
        current.next.prev = current # type: ignore
        self.length -= 1
        return self
    