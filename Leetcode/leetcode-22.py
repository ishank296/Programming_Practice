# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

from typing import List

class Solution:
    def generateParenthesis(self,n: int)->List[str]:
        stk = []
        res = []

        def backtrack(open_nums,close_nums):
            # base case - all parenthesis are added stack
            if open_nums == close_nums == n:
                # add current string to result
                res.append(''.join(stk))
                return

            # condition to check if open parenthesis can be added in string
            if open_nums < n:
                stk.append('(')
                backtrack(open_nums+1,close_nums)
                # cleanup added parenthesis
                stk.pop()

            # condition to check if closed parenthesis can be added in string
            if close_nums < n and close_nums < open_nums:
                stk.append(')')
                backtrack(open_nums,close_nums+1)
                # cleanup added parenthesis
                stk.pop()

        backtrack(0,0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(4))