# Given a string s, find the longest substring without
# repeating characters
# e.g abcabcbb - abc, bbbbbb - 1


class Solution:

    def longestsubstr(self, string: str) -> int:
        if len(string) <= 1:
            return len(string)
        start, end = 0, 0
        max_len = 0
        d = dict()
        while end < len(string):
            if string[end] in d and d[string[end]] >= start:
                start = d[string[end]] + 1
            d[string[end]] = end
            max_len = max(max_len, end - start + 1)
            end +=1
        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.longestsubstr('abcabcbb'))
    print(s.longestsubstr('bbbbb'))
    print(s.longestsubstr('Hello World!'))


