# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
# elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        result = list()
        prefix[0] = 1
        n = len(nums)
        suffix[n-1] = 1
        for idx in range(1,n):
            prefix[idx] = nums[idx-1] * prefix[idx-1]
        for idx in range(n-2,-1,-1):
            suffix[idx] = nums[idx+1] * suffix[idx+1]
        for idx in range(n):
            result.append(prefix[idx] * suffix[idx])
        return result

    def display(self,nums):
        print(f"output for input {nums} is: ",self.productExceptSelf(nums))


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    s = Solution()
    s.display(nums)
    nums = [-1, 1, 0, -3, 3]
    s.display(nums)




