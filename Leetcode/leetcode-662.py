# Maximum width of a Binary Tree
# Maximum width of a binary tree is maximum width
# among all levels
#            4                        1
#          /  \                      / \
#         /    \                    /   \
#        3      6                  2     3
#      /  \      \               /  \   /  \
#     1    8      9             4   5  6    7
#    /
#   2

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def calculatemaxwidth(self, root: TreeNode) -> int:
        max_width = 0
        queue = [(root,1)]
        while queue:
            next_queue = []
            for node in queue:
                if node[0].left is not None:
                    next_queue.append((node[0].left, 2*node[1]))
                if node[0].right is not None:
                    next_queue.append((node[0].right, 2*node[1]+1))
            if len(next_queue) > 0:
                max_width = max(max_width,next_queue[-1][1] - next_queue[0][1]+1)
            queue = next_queue
        return max_width


if __name__ == "__main__":
    val_list = [4, 3, 6, 1, 8, 9, 2]
    node_list = [TreeNode(i) for i in val_list]
    node_list[0].left = node_list[1]
    node_list[0].right = node_list[2]
    node_list[1].left = node_list[3]
    node_list[1].right = node_list[4]
    node_list[2].right = node_list[5]
    node_list[3].left = node_list[6]
    s = Solution()
    print(s.calculatemaxwidth(node_list[0]))









