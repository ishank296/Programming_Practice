# Given the root of a binary search tree, and an integer k,
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_arr = list()
        def inorder(root):
            nonlocal inorder_arr
            if root:
                if root.left:
                    inorder(root.left)
                inorder_arr.append(root.val)
                if root.right:
                    inorder(root.right)
        inorder(root)
        print(inorder_arr)
        return inorder_arr[k-1]