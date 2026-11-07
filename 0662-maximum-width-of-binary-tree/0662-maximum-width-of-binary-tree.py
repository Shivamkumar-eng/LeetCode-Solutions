from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
            
        queue = deque([(root, 0)])
        mx = 0
        
        while queue:
            latest_size = len(queue)
            
            # Identify the boundaries of the current level
            _, start = queue[0]
            _, end = queue[-1]
            mx = max(mx, end - start + 1)
            
            for _ in range(latest_size):
                node, index = queue.popleft()
                
                # Using the updated node.val setup (if needed elsewhere)
                # Left child index: 2 * i + 1
                if node.left:
                    queue.append((node.left, 2 * index + 1))
                # Right child index: 2 * i + 2
                if node.right:
                    queue.append((node.right, 2 * index + 2))
                    
        return mx
