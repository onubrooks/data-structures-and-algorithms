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
                if data < current.value:
                    # if left is None, then insert data
                    if current.left is None:
                        current.left = Node(data)
                        return self
                    # if left is not None, then go left
                    else:
                        current = current.left
                # if data is greater than root, then go right
                elif data > current.value:
                    # if right is None, then insert data
                    if current.right is None:
                        current.right = Node(data)
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

    def BreadthFirstSearch(self):
        current = self.root
        final_list = []
        queue = []
        queue.append(current)

        while len(queue) > 0:
            current = queue.pop(0)
            final_list.append(current.value)
            if current.left:
                queue.append(current.left) # high memory consumption due to adding child nodes to queue
            if current.right:
                queue.append(current.right)

        return final_list
    
    def BreadthFirstSearchRecursive(self, queue, final_list):
        if len(queue) < 1:
            return final_list
        current = queue.pop(0)
        final_list.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        return self.BreadthFirstSearchRecursive(queue, final_list)
    
    def DFTPreOrder(self):
        return traversePreOrder(self.root, [])
    
    def DFTPostOrder(self):
        return traversePostOrder(self.root, [])
    
    def DFTInOrder(self):
        return traverseInOrder(self.root, [])


def traversePreOrder(node, final_list):
    final_list.append(node.value)
    if node.left:
        traversePreOrder(node.left, final_list)
    if node.right:
        traversePreOrder(node.right, final_list)
    return final_list

def traverseInOrder(node, final_list):
    if node.left:
        traverseInOrder(node.left, final_list)
    final_list.append(node.value)
    if node.right:
        traverseInOrder(node.right, final_list)
    return final_list

def traversePostOrder(node, final_list):
    if node.left:
        traversePostOrder(node.left, final_list)
    if node.right:
        traversePostOrder(node.right, final_list)
    final_list.append(node.value)
    return final_list

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print('BFS', tree.BreadthFirstSearch())
print('BFS', tree.BreadthFirstSearchRecursive([tree.root], []))
print('DFSpre', tree.DFTPreOrder())
print('DFSin', tree.DFTInOrder())
print('DFSpost', tree.DFTPostOrder())