class QueueCapacityTypeError(Exception):
    pass

class QueueCapacityBoundError(Exception):
    pass

class QueueIsFull(Exception):
    pass

class QueueIsEmpty(Exception):
    pass

class StackCapacityTypeError(Exception):
    pass

class StackIsFull(Exception):
    pass

class StackIsEmpty(Exception):
    pass

class StackCapacityBoundError(Exception):
    pass

class Node:
    def __init__(self, data=None):
        """ data: contains the data for a given node
        next: contains pointer to next node """
        self.data = data
        self.next = None

class Queue:
    def __init__(self, capacity):
        """ capacity: int between (0, inf) """
        if type(capacity) != int:
            raise QueueCapacityTypeError('Invalid type of capacity')
        elif capacity < 1:
            raise QueueCapacityBoundError('Invalid capacity')
        else:
            self.head = None
            self.tail = None
            self.capacity = capacity
            self.currentSize = 0
        
    def enqueue(self, item):
        '''This method will add an item to the queue. It will then return True/False depending
        on if the enqueue was successful.'''
        if self.isFull():
            raise QueueIsFull("Queue is full")
        
        else:
            new_node = Node(data=item)
            if self.isEmpty():
                self.head = new_node
                self.tail = new_node

            self.tail.next = new_node
            self.tail = new_node
            self.currentSize += 1
            return True
# check
    def dequeue(self):
        '''method will remove an item from the queue and return it'''
        if self.isEmpty():
            raise QueueIsEmpty()
        else:
            head_data = self.head.data
            if self.currentSize == 1:
                self.tail = None
                self.head = None
            else: 
                next_node = self.head.next  # set new node to reference from head
                self.head.next = None       # get rid of reference
                self.head = next_node
            self.currentSize -= 1
            return head_data

    def front(self):
        '''method lets the user peak at the item at the front of the queue without deleting
        it. It will either return the item at the front of the queue or False if the queue is empty'''
        if self.isEmpty():
            return False
        return self.head.data

    def isEmpty(self):
        '''returns True if the queue is empty, otherwise returns False'''
        if self.currentSize == 0:
            return True
        return False

    def isFull(self):
        '''returns True if queue is at capacity, otherwise returns False'''
        if self.currentSize == self.capacity:
            return True
        return False

class Stack:
    def __init__(self, capacity):
        if type(capacity) != int:
            raise StackCapacityTypeError('Invalid type of capacity')
        elif capacity < 1:
            raise StackCapacityBoundError('Invalid capacity')
        else:
            self.head = None
            self.capacity = capacity
            self.currentSize = 0

    def push(self, item):
        '''adds node to the stack and returns True if implemented correctly'''
        if self.isFull():
            raise StackIsFull()
        else:
            new_node = Node(data=item)
            new_node.next = self.head
            self.head = new_node
            self.currentSize += 1
            return True
# check
    def pop(self):
        '''method will remove an item from the stack and return it'''
        if self.isEmpty():
            raise StackIsEmpty()
        else:
            head_data = self.head.data
            head_temp = self.head
            self.head = self.head.next
            head_temp.next = None
            self.currentSize -= 1
            return head_data

    def peek(self):
        '''returns head of Stack data or raises an error if Stack is empty'''
        if self.isEmpty():
            return False
        return self.head.data

    def isEmpty(self):
        '''returns True if current size of Stack is 0, otherwise returns False'''
        if self.currentSize == 0:
            return True
        return False
        
    def isFull(self):
        '''returns True if capacity of stack is full, otherwise returns False'''
        if self.currentSize == self.capacity:
            return True
        return False