class stack:
    def __init__(self):
        self.elements = []  # Stack elements
        self.stack_pointer = -1  # Stack pointer points to the top of the stack

    def push(self, num):
        self.stack_pointer += 1  # Increment the stack pointer
        self.elements.append(num)  # Append the new element to the stack

    def pop(self):
        if self.stack_pointer >= 0:  # Check if the stack is not empty
            self.elements.pop()  # Remove the top element from the stack
            self.stack_pointer -= 1  # Decrement the stack pointer

    def top(self):
        if self.stack_pointer >= 0:  # Check if the stack is not empty
            return self.elements[self.stack_pointer]  # Return the top element of the stack
        return None

    def isEmpty(self):
        return self.stack_pointer == -1  # Return True if the stack is empty, False otherwise

    def size(self):
        return self.stack_pointer + 1  # Return the size of the stack

    def print_stack(self):
        if self.stack_pointer >= 0:  # Check if the stack is not empty
            for i in range(self.stack_pointer, -1, -1):
                print(self.elements[i], end=" ")
            print("")


# Example usage:
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.print_stack()  # Output: 3 2 1

s.pop()
print(s.top())  # Output: 2

print(s.isEmpty())  # Output: False

print(s.size())  # Output: 2
