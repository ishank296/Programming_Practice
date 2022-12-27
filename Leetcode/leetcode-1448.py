# Given a binary tree root, a node X in the tree is named good if
# in the path from root to X there are no nodes with a value greater than X.
#
# Return the number of good nodes in the binary tree.

class Treenode:

    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def goodNodes(self,root: Treenode)->int:
        def helper(root:Treenode,max_val:int):
            res = 0
            if root is None: return res
            if root.val >= max_val: res=1
            max_val = max(max_val,root.val)
            return res + helper(root.left,max_val) + helper(root.right,max_val)
        return 1 + helper(root.left, root.val) + helper(root.right, root.val)