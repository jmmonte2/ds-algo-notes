'''
Assume the end of queue occurs at end of list (index=0)
'''

class Queue:

    # need to assign a list to it
    def __init__(self):
        self.items = []

    # check if queue is empty
    def isempty(self):
        return self.items == []

    # add item to queue
    def enqueue(self, item):
        self.items.insert(0, item)

    # remove item from queue (element @ front of queue)
    def dequeue(self):
        self.items.pop()
    
    # find size of queue
    def size(self):
        return len(self.items)

    




