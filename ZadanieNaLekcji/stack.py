class Stack:
    def __init__(self):
        self.items = []
    def __str__(self):
        return str(self.items)
    def is_empty(self):
        return not self.items
    def is_full(self):
        return False
    def push(self, item):
        self.items.append(item)
    def pop(self):                      
        return self.items.pop()