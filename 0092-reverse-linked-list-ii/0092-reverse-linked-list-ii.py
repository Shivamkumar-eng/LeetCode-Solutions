# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        for _ in range(left-1):
            prev=prev.next

        current=prev.next

        for _ in range(right-left):
            next_node=current.next
            current.next=next_node.next
            next_node.next=prev.next
            prev.next=next_node

        return dummy.next