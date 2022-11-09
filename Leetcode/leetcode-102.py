# Binary Tree Level order Traversal
#       -0
#      /   \
#    -3     -7
#      \   /  \
#     -6  -9   -2
#
#  [[0], [3,7], [6,9,2]]

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelordertraversal(self,root)->list[int]:
        queue = [root]
        result = []
        next_queue = []
        cur_level = []
        while queue:
            for node in queue:
                cur_level.append(node.val)
                if node.left is not None:
                    next_queue.append(node.left)
                if node.right is not None:
                    next_queue.append(node.right)
            result.append(cur_level)
            queue = next_queue
            next_queue = []
            cur_level = []
        return result


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
    print(s.levelordertraversal(root))


