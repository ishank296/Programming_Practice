# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.
from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)-1):
            elem_set = set()
            for j in range(i+1,len(nums)):
                if -1*(nums[i] + nums[j]) in elem_set:
                    res = tuple(sorted([nums[i],nums[j],-1* (nums[i] + nums[j])]))
                    result.add(res)
                #print("i,j: ",i,j)
                #print(" elem set: ",elem_set)
                elem_set.add(nums[j])
        return result

    def display(self,nums):
        print(f"Result for input {nums} is ",self.threeSum(nums))


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    s.display(nums)