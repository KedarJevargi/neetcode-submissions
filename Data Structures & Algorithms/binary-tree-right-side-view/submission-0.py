# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        
        if not root:
            return []
        
        ans = []
        temp = []
        queue = deque([(root, 0)])  
        prev_lev = 0

        while queue:
            c_node, level = queue.popleft()   
            
            if level != prev_lev:
                ans.append(temp[-1])            
                temp = []
                prev_lev = level
            
            temp.append(c_node.val)           

            if c_node.left:
                queue.append((c_node.left, level + 1))   
            if c_node.right:
                queue.append((c_node.right, level + 1))

        ans.append(temp[-1])  
        return ans
