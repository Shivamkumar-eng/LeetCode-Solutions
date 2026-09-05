class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find the middle using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half (using the exact same pointer-flipping logic)
        prev = None
        current = slow
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            
        # Step 3: Compare the first half (head) and the reversed second half (prev)
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True