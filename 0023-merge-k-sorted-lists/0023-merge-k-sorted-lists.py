# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        elements=[]
        if not lists:
            return None
        for head in lists:
            current=head
            while current:
                elements.append(current.val)
                current=current.next
        elements.sort()
        if not elements:
            return None
        head=ListNode(elements[0])
        current=head
        for i in range(1,len(elements)):
            current.next=ListNode(elements[i])
            current=current.next
        return head