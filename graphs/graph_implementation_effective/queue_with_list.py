class queue:
    def __init__(self):
        self.elements = []
        self.front = None
        self.end = None
        
    def enqueue(self, num: "int"):
        if not self.elements:
            self.elements.append(num)
            self.front = 0
            self.end = 0
        else:
            self.elements.append(num)
            self.end += 1
    
    def dequeue(self):
        self.front += 1
    
    def top(self):
        return self.elements[self.front]
    
    def is_empty(self):
        return self.front > self.end
    
    def print_queue(self):
        start = self.front
        while start <= self.end:
            print(self.elements[start], end=" ")
            start += 1
        print("")
            

def main():
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    
    q.print_queue()
    print("queue top", q.top())
    q.dequeue()
    q.enqueue(3)
    q.print_queue()
    print("is_empty: ", q.is_empty())
    
    
if __name__ == "__main__":
    main()
