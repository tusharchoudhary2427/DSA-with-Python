'''Stacks -> In this we can store any type of datatypes. It follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out)'''

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


