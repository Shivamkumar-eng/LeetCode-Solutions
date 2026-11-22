# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while prev.next and prev.next.next:
            first=prev.next
            second=first.next
            next_pair=second.next

            second.next=first
            first.next=next_pair
            prev.next=second

            prev=first
        return dummy.next