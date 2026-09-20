class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sub = []
        t = []

        def preorder(node, array):
            if not node:
                array.append(None)
                return
            array.append(node.val)
            preorder(node.left, array)
            preorder(node.right, array)


        preorder(subRoot, sub)
        preorder(root, t)

        n = len(sub)
        m = len(t)


        windows = []
        for i in range(m - n + 1):
            windows.append(t[i:i+n])

        for w in windows:
            if w == sub:
                return True

        return False
