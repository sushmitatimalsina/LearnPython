stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)

element = stack.pop()
print("Popped element:", element)
print("stack after pop:", stack)

topElement = stack[-1]
print("Top element:", topElement)
print("stack after top element:", stack)
print("Is stack empty?", len(stack) == 0)
print("Stack size:", len(stack))


