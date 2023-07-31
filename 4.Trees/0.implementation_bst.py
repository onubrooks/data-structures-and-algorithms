class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # if root is None, then create root node
        if self.root is None:
            self.root = Node(data)
        else:
            # if root is not None, then find the place to insert
            current = self.root
            while True:
                # if data is less than root, then go left
                if data < self.root.value:
                    # if left is None, then insert data
                    if self.root.left is None:
                        self.root.left = Node(data)
                        return self
                    # if left is not None, then go left
                    else:
                        current = current.left
                # if data is greater than root, then go right
                elif data > self.root.data:
                    # if right is None, then insert data
                    if self.root.right is None:
                        self.root.right = Node(data)
                        return self
                    # if right is not None, then go right
                    else:
                        current = current.right
                # if data is equal to root, then return False
                else:
                    return False

    def search(self, data):
        # if root is None, then return False
        if self.root is None:
            return False
        else:
            # if root is not None, then find the node
            current = self.root
            while current:
                # if data is less than root, then go left
                if data < self.root.value:
                    # if left is None, then return False
                    if self.root.left is None:
                        return False
                    # if left is not None, then go left
                    else:
                        current = current.left
                # if data is greater than root, then go right
                elif data > self.root.data:
                    # if right is None, then return False
                    if self.root.right is None:
                        return False
                    # if right is not None, then go right
                    else:
                        current = current.right
                # if data is equal to root, then return True
                else:
                    return True
            return False

    def remove(self, data):
        pass