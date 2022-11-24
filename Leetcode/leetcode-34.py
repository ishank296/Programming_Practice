#Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
#If target is not found in the array, return [-1, -1].

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = 0
        end = len(nums)-1
        first , last = -1, -1
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        if len(nums) == 1 and nums[0] != target:
            return [-1,-1]
        while (start <= end):
            mid = (end + start) //2
            print("mid: ",mid)
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                first,last = mid,mid
                print("mid:: ",mid)
                while (first > 0 and nums[first-1] == target):
                    first -= 1
                while ( last < len(nums)-1 and nums[last + 1] == target):
                    last +=1
                break
        return [first,last]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([1,4],4))