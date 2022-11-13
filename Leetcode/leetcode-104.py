# Maximum depth of a binary tree
# Given the root of Binary Tree, return its maximum size

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def maxdepth(self,root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxdepth(root.left),
                       self.maxdepth(root.right))


if __name__ == "__main__":
    n1 = TreeNode(3)
    n1.left = TreeNode(9)
    n1.right = TreeNode(20)
    n1.right.left = TreeNode(15)
    n1.right.right = TreeNode(7)
    s = Solution()
    print(s.maxdepth(n1))




