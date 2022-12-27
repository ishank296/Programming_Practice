# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#     1 <---
#    /  \
#   2    3 <----
#   \     \
#   5      4 <---
# output = [1,3,4]

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_order = []
        if root:
            cur_level = [root]
        else: return []
        while cur_level:
            level_order.append([i.val for i in cur_level])
            next_level =[]
            for node in cur_level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            cur_level = next_level
        print(level_order)
        return [l[-1] for l in level_order]

