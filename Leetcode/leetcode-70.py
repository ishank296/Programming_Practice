# climbing stairs
# Number of distinct ways we can climb stairs.it takes n steps to reach top
# Each time we can either climb 1 or 2 steps


class Solution:

    def climbstairs(self,n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n < 0:
            return 0
        return self.climbstairs(n-1) + self.climbstairs(n-2)


if __name__ == "__main__":
    s = Solution()
    print(s.climbstairs(2))
    print(s.climbstairs(3))
    print(s.climbstairs(4))
    print(s.climbstairs(5))

