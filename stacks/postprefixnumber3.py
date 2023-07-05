# Function to check if a character is an operator
def is_operator(char):
    return char in ['+', '-', '*', '/', '^']

# Function to compare the precedence of two operators
def compare_precedence(op1, op2):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence[op1] >= precedence[op2]

# Function to convert infix expression to postfix notation
def infix_to_postfix(expression):
    stack = []
    postfix = []

    for char in expression:
        if char.isalpha():
            postfix.append(char)  # Operand, add to postfix expression
        elif char == '(':
            stack.append(char)  # Opening parenthesis, push to stack
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())  # Pop operators from stack to postfix until opening parenthesis
            if stack and stack[-1] == '(':
                stack.pop()  # Discard opening parenthesis
        elif is_operator(char):
            while stack and stack[-1] != '(' and compare_precedence(stack[-1], char):
                postfix.append(stack.pop())  # Pop operators from stack to postfix until lower precedence operator
            stack.append(char)  # Push current operator to stack

    while stack:
        postfix.append(stack.pop())  # Append remaining operators from stack to postfix

    return ''.join(postfix)

# Function to convert infix expression to prefix notation
def infix_to_prefix(expression):
    stack = []
    prefix = []

    for char in reversed(expression):
        if char.isalpha():
            prefix.append(char)  # Operand, add to prefix expression
        elif char == ')':
            stack.append(char)  # Closing parenthesis, push to stack
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())  # Pop operators from stack to prefix until closing parenthesis
            if stack and stack[-1] == ')':
                stack.pop()  # Discard closing parenthesis
        elif is_operator(char):
            while stack and stack[-1] != ')' and compare_precedence(stack[-1], char):
                prefix.append(stack.pop())  # Pop operators from stack to prefix until lower precedence operator
            stack.append(char)  # Push current operator to stack

    while stack:
        prefix.append(stack.pop())  # Append remaining operators from stack to prefix

    return ''.join(reversed(prefix))

# Testing the code with the given expressions
expression_a = "(((A + B) * C) - D) / F"
expression_b = "((P + ((Q ^ R) - S)) * (U - (P / R)))"

postfix_a = infix_to_postfix(expression_a)
postfix_b = infix_to_postfix(expression_b)

prefix_a = infix_to_prefix(expression_a)
prefix_b = infix_to_prefix(expression_b)

print("Expression a (Infix):", expression_a)
print("Postfix notation:", postfix_a)
print("Prefix notation:", prefix_a)
print()

print("Expression b (Infix):", expression_b)
print("Postfix notation:", postfix_b)
print("Prefix notation:", prefix_b)
