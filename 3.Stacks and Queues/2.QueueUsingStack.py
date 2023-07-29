class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        self.stack1.append(data)

    def dequeue(self):
        if len(self.stack1) > 0:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()