# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def printList(self, l1):
        print(f"Printing List")
        curr = l1
        while curr:
            print(curr.val, end=",")
            curr = curr.next
        print()

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        dummy = newList
        
        carry = 0
        while l1 or l2 or carry:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            val = first + second + carry

            carry = val // 10
            val = val % 10
            
            dummy.next = ListNode(val)
            
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            dummy = dummy.next

        return newList.next