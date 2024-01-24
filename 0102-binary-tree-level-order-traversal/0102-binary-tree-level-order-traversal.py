# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        visited = []
        
        if root is None:
            return []
        
        q = deque()
        q.append((root, 1))
        
        while q:
            cur_node, cur_depth = q.popleft()
            
            visited.append((cur_node.val, cur_depth))
            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))
                
        dic = {}
        
        for tup in visited:
            val = tup[1]
            level = tup[0]
            if val in dic:
                dic[val].append(level)
            else:
                dic[val] = [level]
        
        return list(dic.values())