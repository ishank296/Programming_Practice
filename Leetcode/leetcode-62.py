# unique paths to travel from start to end of m x n matrix
# where only possible choices are to go a step right or down in matrix.


class Solution:

    def uniquepaths(self,m: int, n: int) -> int:
        if m == n == 1:
            return 1
        dp = list()
        for i in range(m):
            dp.append(list())
            for j in range(n):
                dp[i].append(0)
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for row in range(1,m):
            for col in range(1,n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        print('')
        for i in range(m):
            for j in range(n):
                print(dp[i][j],end=' ')
            print('')
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    s.uniquepaths(3,4)
    s.uniquepaths(4, 4)


