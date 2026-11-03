# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current3 = dummy
        carry = 0
        
        # Loop runs if either list has elements, OR if there is a remaining carry
        while l1 or l2 or carry:
            # Extract values if nodes exist; otherwise, use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            ans = total % 10
            
            # Create the new node and move forward
            current3.next = ListNode(ans)
            current3 = current3.next
            
            # Move list pointers forward if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy.next
