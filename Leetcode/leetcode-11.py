# Given n non-negative integers where each represents points in coordinates
# n vertica lines are drawn such that two endpoints of the line i at (i,a) and
# (i,0), Find the two lines which together with the x-axis forms a container
# tha contains most water

class Solution:

    def maxarea(self,height: list[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            area = min(height[start], height[end]) * (end-start)
            max_area = max(area, max_area)
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1
        return max_area


if __name__ == "__main__":
    h = [1,8,6,3,5,4,8,3,7]
    s = Solution()
    print(s.maxarea(h))