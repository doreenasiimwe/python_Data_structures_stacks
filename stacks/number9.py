class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to store stack elements

    def is_empty(self):
        return len(self.stack) == 0  # Check if the stack is empty

    def push(self, item):
        self.stack.append(item)  # Add an item to the top of the stack

    def pop(self):
        if self.is_empty():
            return None  # If the stack is empty, return None
        return self.stack.pop()  # Remove and return the top item from the stack

    def peek(self):
        if self.is_empty():
            return None  # If the stack is empty, return None
        return self.stack[-1]  # Return the top item from the stack without removing it

    def size(self):
        return len(self.stack)  # Return the number of elements in the stack


def check_balanced_parentheses(expression):
    stack = Stack()  # Create an instance of the Stack class
    opening_brackets = ['(', '[', '{']  # List of valid opening brackets
    closing_brackets = [')', ']', '}']  # List of corresponding closing brackets

    for char in expression:
        if char in opening_brackets:
            stack.push(char)  # Push opening brackets onto the stack
        elif char in closing_brackets:
            if stack.is_empty():
                return False  # If there is a closing bracket without a corresponding opening bracket, return False
            top = stack.pop()  # Pop the top element from the stack
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False  # If the closing bracket does not match the corresponding opening bracket, return False

    return stack.is_empty()  # Check if all opening brackets have been matched and the stack is empty


# Testing the balanced parentheses checker
expression1 = "{(a + b) * [c - d]}"
expression2 = "[(a + b) * (c - d]"
expression3 = "(a + b) * [c - d)]"
expression4 = "(a + b) * [c - d]"

print("Expression:", expression1)
print("Balanced parentheses:", check_balanced_parentheses(expression1))

print("Expression:", expression2)
print("Balanced parentheses:", check_balanced_parentheses(expression2))

print("Expression:", expression3)
print("Balanced parentheses:", check_balanced_parentheses(expression3))

print("Expression:", expression4)
print("Balanced parentheses:", check_balanced_parentheses(expression4))
