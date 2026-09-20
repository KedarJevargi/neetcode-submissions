from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        temp = []
        queue = deque([(root, 0)])  # use root, not head
        prev_lev = 0

        while queue:
            c_node, level = queue.popleft()   # unpack tuple
            
            if level != prev_lev:
                ans.append(temp)            
                temp = []
                prev_lev = level
            
            temp.append(c_node.val)           # store value

            if c_node.left:
                queue.append((c_node.left, level + 1))   # wrap in tuple
            if c_node.right:
                queue.append((c_node.right, level + 1))

        ans.append(temp)   # flush the last level
        return ans
