class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):

            if not node:
                return 0

            left_height = 0
            right_height = 0

            if node.left:
                left_height = dfs(node.left)

            if node.right:
                right_height = dfs(node.right)

            return 1 + max(left_height, right_height)

        return dfs(root)

