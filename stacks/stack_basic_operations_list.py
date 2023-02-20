class stack:
    def __init__(self):
        self.elements = []
        self.stack_pointer = -1

    def push(self, num: "int"):
        print("Pushing to stack: ", num)
        self.stack_pointer += 1
        self.elements.append(num)
    
    def pop(self):
        print("Popping from stack")
        self.stack_pointer -= 1
    
    def top(self):
        print("Peek from stack")
        if not self.elements:
            return None

        return self.elements[self.stack_pointer]
    
    def isEmpty(self):
        print("Checking whether stack is empty or not")
        return len(self.elements) == 0
        
    def print_stack(self):
        temp = self.stack_pointer
        print("Printing Stack")
        while temp > -1:
            print(self.elements[temp], end=" ")
            temp -= 1
        print("")
        
    def size(self):
        print("Stack size is: ", end="")
        size = 0
        temp = self.stack_pointer
        while temp > -1:
            temp -= 1
            size += 1
            
        return size
    
def main():
    s = stack()
    s.push(1)
    s.push(2)
    
    s.print_stack()
    s.pop()
    s.print_stack()
    s.pop()
    s.print_stack()
    s.push(1)
    s.push(2)
    s.print_stack()
    print(s.top())
    print(s.isEmpty())
    print(s.size())
    

if __name__ == "__main__":
    main()
