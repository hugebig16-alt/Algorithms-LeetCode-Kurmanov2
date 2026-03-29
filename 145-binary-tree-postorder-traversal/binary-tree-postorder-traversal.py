class Solution:
    def postorderTraversal(self, root):
        res = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)         # лево
            dfs(node.right)        # право
            res.append(node.val)   # корень
        
        dfs(root)
        return res