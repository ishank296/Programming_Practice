# House Robber
# Given an integer array of nums representing the amount of money
# representing the money of each house,return the maximum amount of money
# that can be robbed given that no two adjacent houses can be robbed

class Solution:

    def rob(self,nums: list[int])->int:
        if len(nums) == 1:
            return nums[0]
        res = [nums[0]]
        for house in range(1,len(nums)-1):
            if house == 1:
                res.append(max(nums[house],nums[house-1]))
            else:
                res.append(max(nums[house] + res[house-2],res[house-1]))
        return res[-1]


if __name__ == "__main__":
    s = Solution()
    nums = [1,9,1,1,9,1]
    print(s.rob(nums))