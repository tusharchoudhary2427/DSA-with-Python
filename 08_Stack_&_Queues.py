'''Stacks -> In this we can store any datatypes. It follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out)'''

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Can't pop"
        x = self.items.pop()
        return x
    
    def top(self):
        if len(self.items) == 0:
            return "Can't top"
        return self.items[-1]
    
    def size(self):
        return len(self.items)

stack = Stack()
stack.push(10)
stack.push(5)
stack.push(50)

print(stack.pop())
print(stack.pop())
print(stack.top())
print(stack.size())
print(stack.is_empty())

# TC -> For push, pop, TOP, and is_empty time complexity will be O(1), whether it is best/avg or worst. and for SC -> O(n) 


'''Queues -> It is a linear Data Structure and it is used for storing and managing data in a specific order. It follows the principle of "First in, First out" (FIFO), where the first element added to the queue is the first one to be removed '''

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("Dequeue from empty queue")
            return None
        return self.items.pop(0)
        
    def front(self):
        if self.is_empty():
            return None
        return self.items[0]
    
    def rear(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    

queue = Queue()
queue.enqueue(12)
queue.enqueue(14)
queue.enqueue(16)
queue.enqueue(18)
queue.enqueue(20)

print(queue.dequeue())  
print(queue.front())    
print(queue.rear())     
print(queue.size())     
print(queue.is_empty()) 

# TC -> For enqueue, is_empty, front, rear, size it is O(1), but for dequeue it is O(n), because all the elements will shift to there because it will pop from 0th index and the TC will be same for best/avg or worst, and  SC -> O(n) 

'''Deque -> It stands for Double Ended Queue, is a special type of queue that allows adding and removing elements from both front and rear ends.'''

from collections import deque

lst = deque([10,20,30])

lst.append(40)

lst.appendleft(5)
lst.extend([50,60,70])
print("After extending :", lst)

lst.extendleft([0,1])
print("After extending left :", lst)

lst.remove(1)
print("After removing :", lst)

lst.pop()

print(lst)


'''Implementing Stacks using Queues -> '''

from collections import deque

class StackusingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self,item):
        self.queue.append(item)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue.popleft()
    
    def top(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        return list(self.queue)
    
# TC -> for push and display it is O(n) and for pop, top, is_empty, size and display it is O(1) as only 1 operation is performing there, the SC-> is O(1) for every operation.
    
s = StackusingQueue()

s.push(10)
s.push(20)
s.push(30)

print(s.display())
print(s.pop())
print(s.is_empty())


'''Implementing Queues using Stacks -> '''

class QueueStack:
    def __init__(self):
        self.st1 = []   
        self.st2 = []   

    def enqueue(self, item):   
        self.st1.append(item)

    def dequeue(self):         # Remove from front
        if not self.st1 and not self.st2:
            print("Queue is empty")
            return -1

        if not self.st2:   # transfer only when st2 is empty
            while self.st1:
                self.st2.append(self.st1.pop())

        return self.st2.pop()

    def front(self):           
        if not self.st1 and not self.st2:
            print("Queue is empty")
            return -1

        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())

        return self.st2[-1]
    
    def rear(self):
        if not self.st1 and not self.st2:
            print("Queue is empty")
            return -1
        
        if self.st1:
            return self.st1[-1]
        else:
            return self.st2[0]

    def is_empty(self):
        return not self.st1 and not self.st2


# TC-> for enqueue it is O(1), for dequeue it is O(1) for best/avg case and for worst it is O(n) and for is_empty, front it will be O(n) and the SC -> will be O(1).


q = QueueStack()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.front())
print(q.rear())
print(q.is_empty())


