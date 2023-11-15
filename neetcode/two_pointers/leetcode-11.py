# Container With Most Water.
# You are given an integer array height of length n. There are n vertical lines drawn
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        start,end=0,len(height)-1
        max_area=0
        while start < end:
            area = (end - start) * min(height[start],height[end])
            max_area = max(area,max_area)
            if height[start] < height[end]:
                start+=1
            else:
                end-=1
        return max_area

    def display(self,height):
        print(f"result for input {height} is: ",self.maxArea(height))


if __name__ == "__main__":
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s.display(height)




