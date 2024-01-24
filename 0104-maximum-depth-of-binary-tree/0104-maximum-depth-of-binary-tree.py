# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        if root is None:
            return max_depth
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        max_depth = max(left, right) + 1
        
        return max_depth
        