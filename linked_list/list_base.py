class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Slist:

    def __init__(self):
        self._first = None

    def print_list(self):
        current = self._first
        while current:
            print(current.val, end="->")
            current = current.next

        print("->NULL", end="\n")

    def build_list_from_list(self, num_list: "list"):
        for num in num_list:
            new = ListNode(num)
            if not self._first:
                self._first = new
            else:
                current = self._first
                while current.next:
                    current = current.next

                current.next = new

    def rotate(self, k: "number of positions"):
        current = self._first
        counter = 1
        # iterate the whole list, count the length
        # Change the last nodes next to first
        while current.next:
            counter += 1
            current = current.next

        current.next = self._first

        # k should be updated, because
        # if k is equal to length that means, no rotations,
        # if k is 6 and length is 5 that means 1 rotation
        k = k % counter
        # iterate till length - k - 1 node
        # So that we can cut the cycle
        k_counter = 0
        current = self._first
        while k_counter < counter - k - 1:
            current = current.next
            k_counter += 1

        self._first = current.next
        current.next = None
