class Solution:
    def preorderTraversal(self, root):
        res = []
        
        def dfs(node):
            if not node:
                return
            res.append(node.val)   # сначала корень
            dfs(node.left)         # потом лево
            dfs(node.right)        # потом право
        
        dfs(root)
        return res