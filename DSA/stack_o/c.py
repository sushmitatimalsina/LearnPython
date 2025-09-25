class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element) 

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack. pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)== 0
    
    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print("stack after push:", stack.stack)  

print("Popped element:", stack.pop())
print("stack after pop:", stack.stack)
print("peek element:", stack.peek())
print("Is stack empty?", stack.isEmpty())
print("Stack size:", stack.size())