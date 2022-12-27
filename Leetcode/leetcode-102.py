# Binary Tree Level order Traversal
#       -0
#      /   \
#    -3     -7
#      \   /  \
#     -6  -9   -2
#
#  [[0], [3,7], [6,9,2]]

from typing import List,Optional

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root:
            cur_level = [root]
        else:
            return []
        while cur_level:
            res.append([i.val for i in cur_level])
            next_level = []
            for i in cur_level:
                if i.left: next_level.append(i.left)
                if i.right: next_level.append(i.right)
            cur_level = next_level
        return res


if __name__ == "__main__":
    root = TreeNode(0)
    t1 = TreeNode(3)
    t2 = TreeNode(7)
    t3 = TreeNode(6)
    t4 = TreeNode(9)
    t5 = TreeNode(2)
    root.left = t1
    root.right = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    s = Solution()
    print(s.levelOrder(root))


