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

    while stack and stack[-1] != '(':
        postfix.append(stack.pop())  # Append remaining operators from stack to postfix

    return ''.join(postfix)

# Testing the code with the given expression
infix_expression = "((A - (B / C)) ^ D) / (E - F)"
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix expression:", postfix_expression)
