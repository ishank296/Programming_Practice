# Given the roots of two binary trees root and subRoot, return true if
# there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree [tree] is a tree that consists of a node in tree and
# all of this node's descendants. The tree [tree] could also be considered as a subtree of itself.


class Tree:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubTree(self,root,subRoot)->bool:

        def isSame(root,subRoot):
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False
            if root.val == subRoot.val:
                return isSame(root.left,subRoot.left) and \
                isSame(root.right,subRoot.right)

        if isSame(root,subRoot):
            return True
        if self.isSubTree(root.left,subRoot) or self.isSubTree(root.right,subRoot):
            return True
        return False


