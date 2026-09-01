# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        address_set=set()
        current=head
        while current:
            if current not in address_set:
                address_set.add(current)
                current=current.next
            else:
                return True
        return False