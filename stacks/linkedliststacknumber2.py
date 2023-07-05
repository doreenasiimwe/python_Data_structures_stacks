class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot perform pop operation.")
            return None
        else:
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot perform peek operation.")
            return None
        else:
            return self.head.data


# Testing the stack operations
stack = Stack()

# Pushing elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Peeking at the top element of the stack
print("Top element of the stack:", stack.peek())

# Popping elements from the stack
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())

# Peeking at the top element after popping all elements
print("Top element of the stack:", stack.peek())
