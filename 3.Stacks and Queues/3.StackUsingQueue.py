class StackUsingQueue:
    def __init__(self):
        self.main_queue = []
        self.temp_queue = []

    def push(self, value):
        while len(self.main_queue) != 0:
            # move all elements from main_queue to temp_queue using shift operation (pop(0))
            self.temp_queue.append(self.main_queue.pop(0))
        self.main_queue.append(value)
        while len(self.temp_queue) != 0:
            # move all elements from temp_queue to main_queue using shift operation (pop(0))
            self.main_queue.append(self.temp_queue.pop(0))

    def pop(self):
        return self.main_queue.pop(0)
    
    def peek(self):
        return self.main_queue[0]
    
    def is_empty(self):
        return len(self.main_queue) == 0
