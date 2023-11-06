# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = dict()
        for num in nums:
            num_dict[num] = num_dict.get(num,0) + 1
        res = sorted([(k,v) for k,v in num_dict.items()],key=lambda x: x[1],reverse=True)
        return [x[0] for x in res[:k]]

    def display(self,nums,k):
        print(f"output for input {nums},k:{k} is: ",self.topKFrequent(nums,k))


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    s = Solution()
    s.display(nums,k)
