'''
    1. Need to store items in lists
    2. Add item to end or front of deque
    3. Remove item from end or front of deque
    4. Size of deque

'''


class Deque():
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)
    
    # O(n) due to insert moving n items
    def add_rear(self, item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    # O(n) since all items will be removed down 1 index
    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
        

    

