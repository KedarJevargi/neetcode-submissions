# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        def cal(root,p,q):
            curr=root.val;
            if not root:
                return None
            elif p<curr and q<curr:
                return cal(root.left,p,q)
            elif p>root.val and q>root.val:
                return cal(root.right,p,q)  
            else:     
            
                return root

        return cal(root,p.val,q.val)             
        


        