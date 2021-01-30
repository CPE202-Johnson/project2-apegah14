# A Stack is a Stack(capacity)
# creates a stack using a Python list
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0 

    # Stack -> boolean
    # checks to see if the stack is empty
    def is_empty(self):
        return self.num_items == 0

    # Stack -> boolean
    # checks to see if the stack is full
    def is_full(self):
        return self.num_items == self.capacity

    # Stack, item -> None
    # pushes given item on the stack
    def push(self, item):
        if self.is_full():                  # if stack is full raise IndexError
            raise IndexError
        self.items[self.num_items] = item   # add item to end of array
        self.num_items += 1                 # increment number of items

    # Stack -> item
    # returns the last item pushed to the stack and removes it from the stack
    def pop(self):
        if self.is_empty():                 # if stack is empty raise IndexError
            raise IndexError
        self.num_items -= 1                 # decrement place in array
        item = self.items[self.num_items]   # temp item variable
        self.items[self.num_items] = None   # removes item from stack
        return item

    # Stack -> item
    # returns the last item pushed to the stack, does not remove it
    def peek(self):
        if self.is_empty():                 # if stack is empty raise IndexError
            raise IndexError
        return self.items[self.num_items - 1]

    # Stack -> int
    # returns number of items currently in stack
    def size(self):
        return self.num_items
