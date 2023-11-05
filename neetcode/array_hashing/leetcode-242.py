# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_occur = [0] * 26
        for char in s:
            char_occur[ord(char) - 97] +=1
        for char in t:
            char_occur[ord(char) - 97] -=1
        for elem in char_occur:
            if elem != 0:
                return False
        return True

    def display(self, s,t):
        print(f"output for inputs {s} and {t} : ",self.isAnagram(s,t))


if __name__ == "__main__":
    s = "rat"
    t = "car"
    S = Solution()
    S.display(s,t)

    s = "anagram"
    t = "nagaram"
    S.display(s, t)
