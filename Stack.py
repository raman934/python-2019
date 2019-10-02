# RG
# 11.2

class Stack:

    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def get_size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)
