## Given a Binary Tree, Print the inorder traversal
## of its nodes values

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self,root: TreeNode) -> list[int]:
        if root is None: return []
        return self.inorderTraversal(root.left) + [root.val] \
               + self.inorderTraversal(root.right)

    def inorderTraversal2(self,root:TreeNode)->list[int]:
        stack = []
        result = []
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result



