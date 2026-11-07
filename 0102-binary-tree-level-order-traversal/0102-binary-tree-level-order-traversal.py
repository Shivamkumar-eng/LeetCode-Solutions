from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
            
        result = []
        # Initialize queue with the root node
        queue = deque([root])
        
        while queue:
            # Get the exact number of nodes at the current level
            level_size = len(queue)
            current_level = []
            
            # Process all nodes belonging to this specific level
            for _ in range(level_size):
                node = queue.popleft()
                
                # Append the value using the updated .val attribute
                current_level.append(node.val)
                
                # Enqueue left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the completed level to our 2D array
            result.append(current_level)
            
        return result
