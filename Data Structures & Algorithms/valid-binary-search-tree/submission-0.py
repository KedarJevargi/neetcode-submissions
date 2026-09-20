# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def cal(root,minn,maxx):
            if not root:
                return True
            if root.val>=maxx or root.val<=minn:
                return False
            return cal(root.left,minn,root.val) and cal(root.right,root.val,maxx)

        return cal(root,float("-inf"), float("inf"))