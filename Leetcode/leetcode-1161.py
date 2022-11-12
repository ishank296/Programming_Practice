# Maximum level sum of a Binary Tree
# smallest level x such that sum of all nodes
# at level x is maximal. level of Root is 1

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        from collections import defaultdict
        self.levelsum = defaultdict(int)

    def maxlevelsum(self,root: TreeNode)-> (int,int):
        max_sum = root.val
        res,level_no = 1, 1
        queue = [root]
        while queue:
            for node in queue:
                next_queue = []
                cur_sum = 0
                cur_sum += node.val
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if cur_sum > max_sum:
                max_sum = cur_sum
                res = level_no
            level_no += 1
            queue = next_queue
        return res,max_sum

    def maxlevelsumrecursive(self,root:TreeNode)->(int,int):
        level = 1
        max_sum = root.val
        res = (1, root.val)
        self.helper(root, level)
        for key, value in self.levelsum.items():
            if max_sum < value:
                res = (key, value)
                max_sum = value
        return res

    def helper(self,root:TreeNode,level:int):
        if root:
            self.levelsum[level] += root.val
        if root.left:
            self.helper(root.left,level+1)
        if root.right:
            self.helper(root.right,level+1)


if __name__ == "__main__":
    n1 = TreeNode(989)
    n1.right = TreeNode(10250)
    n1.right.left = TreeNode(98693)
    n1.right.right = TreeNode(-89388)
    n1.right.right.right = TreeNode(-32127)
    s = Solution()
    print(s.levelsum)
    print(s.maxlevelsum(n1))
    print(s.maxlevelsumrecursive(n1))

