# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # sentinel head to simplify edge cases
        curr = dummy 
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0
            
            sum = val1 + val2 + carry
            carry = sum // 10 # integer division
            digit = sum % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next
        
        return dummy.next