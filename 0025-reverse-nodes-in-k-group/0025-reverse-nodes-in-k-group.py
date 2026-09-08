# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # 1. Check if there are k nodes left to reverse
            kth = self.get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            
            # 2. Reverse the k group
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            # 3. Connect with the previous part and move group_prev
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
            
        return dummy.next

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr