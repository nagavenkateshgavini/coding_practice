class cqueue:
    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.k = k
        self.q = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.q[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.tail - 1]

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
    
    def print_queue(self):
        print(self.q)
        # temp = self.first
        # import pdb;pdb.set_trace()
        # while temp < self.end:
        #     print(self.elements[temp], end=" ")
        #     temp += 1
        # print("")
            

def main():
    cq = cqueue(3)
    cq.enQueue(6)
    cq.print_queue()
    print(cq.Rear())
    cq.enQueue(2)
    cq.enQueue(3)
    cq.enQueue(4)
    
    cq.print_queue()
    print("rear: ", cq.Rear())

if __name__ == "__main__":
    main()
