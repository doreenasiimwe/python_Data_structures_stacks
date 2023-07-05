def evaluate_postfix(expression):
    stack = []  # Initialize an empty stack

    for token in expression.split():
        if token.isdigit():  # If the token is a digit (operand)
            stack.append(int(token))  # Push it onto the stack
        else:  # If the token is an operator
            operand2 = stack.pop()  # Pop the top two operands from the stack
            operand1 = stack.pop()
            result = perform_operation(token, operand1, operand2)  # Perform the operation
            stack.append(result)  # Push the result back onto the stack

    return stack.pop()  # The final result is the top element of the stack


def perform_operation(operator, operand1, operand2):
    if operator == '+':  # Addition operation
        return operand1 + operand2
    elif operator == '-':  # Subtraction operation
        return operand1 - operand2
    elif operator == '*':  # Multiplication operation
        return operand1 * operand2
    elif operator == '/':  # Division operation
        return operand1 / operand2


# Testing the code with the given postfix expression
postfix_expression = "15 3 - 2 * 6 6 / -"
result = evaluate_postfix(postfix_expression)
print("Result:", result)
