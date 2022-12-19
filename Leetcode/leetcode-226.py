# Given the root of a binary tree, invert the tree, and return its root.
#      4                4
#     / \              / \
#    2   7            7   2
#   / \  / \         / \  / \
#  1  3  6  9       9  6  3  1


class TreeNode:

    def __int__(self,val,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def invertTree(self,root):
        def swapchildren(root):
            if root is None:
                return
            root.left,root.right = root.right,root.left
            swapchildren(root.left)
            swapchildren(root.right)
        swapchildren(root)
        return root



