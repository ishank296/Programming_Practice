# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1,2]
        head,tail = 0,len(numbers)-1
        while head < tail:
            if numbers[head] + numbers[tail] == target:
                return [head+1,tail+1]
            if numbers[head] + numbers[tail] > target:
                tail -=1
            if numbers[head] + numbers[tail] < target:
                head +=1

    def display(self,numbers,target):
        print(f"result for input nums: {numbers} and target {target} is : ",self.twoSum(numbers,target))


if __name__ == "__main__":
    numbers = [2, 3, 4]
    target = 6
    s = Solution()
    s.display(numbers,target)
    numbers = [2, 7, 11, 15]
    target = 9
    s.display(numbers,target)
    numbers = [-1, 0]
    target = -1
    s.display(numbers,target)