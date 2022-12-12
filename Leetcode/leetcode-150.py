# 150. Evaluate Reverse Polish Notation
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i in ('+','-','/','*'):
                a,b = stk.pop(),stk.pop()
                if i == '/':
                    res = eval(f"int({b} {i} {a})")
                else:
                    res = eval(f"{b} {i} {a}")
                stk.append(res)
            else:
                stk.append(i)
        return int(stk[-1])