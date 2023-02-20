class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
class Stack:
    def __init__(self):
        self.first = None
        self.end = None
        
    def push(self, num: "int"):
        print("Push to stack, num: ", num)
        new_node = ListNode(num)
        if not self.first:
            self.first = new_node
            self.end = new_node
        else:
            new_node.next = self.first
            self.first = new_node
            
    def pop(self):
        print("Pop from linked list")
        self.first = self.first.next
        
    def top(self):
        print("Peek stack")
        return self.first.val
    
    def is_empty(self):
        return not bool(self.first)
            
    def print_stack(self):
        print("Printing stack")
        current = self.first
        while current:
            print(current.val, end=" ")
            current = current.next
        print("")
            

def main():
    s = Stack()
    s.push(1)
    s.push(2)
    
    s.print_stack()
    
    s.pop()
    s.print_stack()

    print(s.top())
    s.push(2)
    s.pop()
    s.pop()
    s.print_stack()
    print("Is stack empty: ", s.is_empty())

if __name__ == "__main__":
    main()