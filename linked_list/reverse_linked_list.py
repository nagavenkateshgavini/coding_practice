from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        while head:
            next = head.next
            head.next = previous
            previous = head
            head = next

        return previous

ls1 = ListNode(1)
ls2 = ListNode(2)
ls3 = ListNode(3)
ls1.next = ls2
ls2.next = ls3
head = ls1

if __name__ == "__main__":
    s = Solution()
    rev = s.reverseList(head)
    while(True):
      print(rev.val, end=",")
      if(rev.next is None):
        break
      rev = rev.next
    print()

