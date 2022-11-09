# Binary Tree Pre-order traversal
#      5
#     / \
#    3   6
#   / \
#  8   9
#
# 5 3 8 9 6

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def preorderTraversal(self, root:TreeNode) -> list[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + \
            self.preorderTraversal(root.right)

    def preorderTraversal2(self,root:TreeNode)->list[int]:
        stack = []
        result = []
        while root is not None or stack != []:
            while root is not None:
                result.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return result


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(9)
    root.right = TreeNode(6)
    s = Solution()
    result = s.preorderTraversal2(root)
    print(result)


