class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # НАШЛИ узел
            
            # 1. нет левого
            if not root.left:
                return root.right
            
            # 2. нет правого
            if not root.right:
                return root.left
            
            # 3. есть оба ребёнка
            # ищем минимум справа
            min_node = self.getMin(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root
    
    def getMin(self, node):
        while node.left:
            node = node.left
        return node