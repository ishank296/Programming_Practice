# Given the roots of two binary trees p and q,
# write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.

from typing import Optional

class Tree:

    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self,p:Optional[Tree],q:Optional[Tree])->bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left,q.right) and self.isSameTree(p.rigthq.right)