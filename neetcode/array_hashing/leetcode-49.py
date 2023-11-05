# Given an array of strings strs, group the anagrams together.
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = dict()
        for word in strs:
            word_dict[''.join(sorted(word))] = word_dict.get(''.join(sorted(word)),[]) + [word]
        return [value for value in word_dict.values()]

    def display(self,strs):
        print(f"Output for input {strs}: ",self.groupAnagrams(strs))


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    s.display(strs)