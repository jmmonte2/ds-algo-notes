'''
Assume the end of queue occurs at end of list (index=0)
'''

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # O(n) due to insert moving n items
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()
    
    def size(self):
        return len(self.items)

    




