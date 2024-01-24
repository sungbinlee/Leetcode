"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        answer = []
        
        def dfs(root):
            if root is None:
                return None
            
            answer.append(root.val)
            
            for child in root.children:
                dfs(child)
            
        dfs(root)
        
        return answer