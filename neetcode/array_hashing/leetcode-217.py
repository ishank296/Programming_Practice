# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for num in nums:
            if d.get(num,0) > 0 :
                return True
            d[num] = d.get(num,0) +1
        return False

    def display(self, nums):
        print("Result for Input : ", nums, ":")
        print(self.containsDuplicate(nums))


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,1]
    s.display(nums)
    nums = [1,2,3,4]
    s.display(nums)

