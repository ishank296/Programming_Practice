# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


class Tree:

    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right= right


class Solution:

    def diameterOfBinaryTree(self,root)->int:
        max_dia = 0
        def dfs(root):
            nonlocal max_dia
            if root is None:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            max_dia = max(max_dia,left_height + right_height)
            return 1 + max(dfs(root.left),max(root.right))
        dfs(root)
        return max_dia