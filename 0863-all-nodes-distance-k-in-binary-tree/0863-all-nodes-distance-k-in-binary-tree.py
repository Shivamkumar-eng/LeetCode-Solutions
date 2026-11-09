from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root or not target:
            return []
            
        # Step 1: Track parents of every node using BFS
        parent_map = {}
        queue = deque([root])
        
        while queue:
            current = queue.popleft()
            if current.left:
                parent_map[current.left] = current
                queue.append(current.left)
            if current.right:
                parent_map[current.right] = current
                queue.append(current.right)
                
        # Step 2: Radial BFS from the target node
        bfs_queue = deque([target])
        visited = {target}
        curr_level = 0
        
        while bfs_queue:
            if curr_level == k:
                break
                
            for _ in range(len(bfs_queue)):
                current = bfs_queue.popleft()
                
                # Check left, right, and parent directions
                for neighbor in (current.left, current.right, parent_map.get(current)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        bfs_queue.append(neighbor)
                        
            curr_level += 1
            
        # Step 3: Elements left in queue are exactly at distance k
        return [node.val for node in bfs_queue]
