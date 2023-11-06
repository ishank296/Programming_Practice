# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = dict()
        for idx in range(len(nums)):
            if (nums[idx]) in sum_dict.keys():
                return [sum_dict[nums[idx]],idx]
            sum_dict[target-nums[idx]] = idx
        print(sum_dict)
        return []

    def display(self,nums,target):
        print(f"Output for nums: {nums} and target: {target} is ",self.twoSum(nums,target))


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    s.display(nums,target)

    nums = [3, 2, 4]
    target = 6
    s.display(nums, target)