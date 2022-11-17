# Given a m x n grid filled with non-negative numbers, find a path
# from top left to bottom right, which minimizes the sum of all numbers
# along its path
# we can only move either down or right at any point in time


class Solution:

    def minpathsum(self, grid: list[list[int]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        if num_row == num_col == 1:
            return grid[0][0]
        dp = list()
        for i in range(num_row):
            dp.append(list())
            for j in range(num_col):
                dp[i].append(0)
        dp[0][0] = grid[0][0]
        for i in range(1,num_row):
            dp[i][0] = grid[i][0]+dp[i-1][0]
        for j in range(1,num_col):
            dp[0][j] = grid[0][j]+dp[0][j-1]
        for row in range(1,num_row):
            for col in range(1,num_col):
                dp[row][col] = min(dp[row-1][col] , dp[row][col-1]) + grid[row][col]

        print('')
        for i in range(num_row):
            for j in range(num_col):
                print(dp[i][j], end=' ')
            print('')
        return dp[-1][-1]


if __name__ == "__main__":
    grid = [
        [1,1,4,6],
        [2,6,2,1],
        [3,7,1,1]
    ]
    s = Solution()
    s.minpathsum(grid)

