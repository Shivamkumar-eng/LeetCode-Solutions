# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        current2=dummy
        current=head
        l=[]
        while current:
            l.append(current.val)
            current=current.next
        l.sort()
        for i in l:
            current2.next=ListNode(i)
            current2=current2.next
        return dummy.next