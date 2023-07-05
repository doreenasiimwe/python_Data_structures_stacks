class Stack:
    def __init__(self):
        self.stack = []     # Create an empty list to serve as the stack
        self.top = -1       # Initialize the top pointer to -1 (indicating an empty stack)

    def push(self, element):
        self.top += 1       # Increment the top pointer by 1
        self.stack.append(element)    # Add the element to the end of the stack list

    def pop(self):
        if self.is_empty():   # Check if the stack is empty
            print("Stack Underflow")    # Display an underflow error message
            return None
        else:
            element = self.stack[self.top]    # Retrieve the element pointed by the top
            self.top -= 1       # Decrement the top pointer by 1
            return element

    def peek(self):
        if self.is_empty():    # Check if the stack is empty
            print("Stack Underflow")    # Display an underflow error message
            return None
        else:
            return self.stack[self.top]   # Return the element pointed by the top

    def is_empty(self):
        return self.top == -1   # Check if the top pointer is -1, indicating an empty stack
stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print(stack.pop())  # Output: 15
print(stack.peek())  # Output: 10


