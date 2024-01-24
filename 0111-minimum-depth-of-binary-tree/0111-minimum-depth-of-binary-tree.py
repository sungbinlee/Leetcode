# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        leaf_nodes = []
        if root is None:
            return 0
        
        q = deque()
        q.append((root, 1))
        
        while q:
            cur_node, cur_depth = q.popleft()
            
            if cur_node.left is None and cur_node.right is None:
                leaf_nodes.append(cur_depth)
                
            if cur_node.left:
                q.append((cur_node.left,cur_depth + 1))
            if cur_node.right:
                q.append((cur_node.right,cur_depth + 1))
        
        return min(leaf_nodes)