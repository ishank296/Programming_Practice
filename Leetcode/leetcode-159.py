# Given a string s, find the length of the longest substring t that contains
# at most 2 distinct characters
# e.g "eceba" output - 3 (ece)

class Solution:

    def longestsubstrtwodistinctchars(self, string: str):
        if len(string) < 3:
            return len(string)
        max_len = 1
        start,end = 0,1
        chars = dict()
        while end < len(string):
            if string[end] not in chars:
                if len(chars) < 2:
                    chars[string[end]] = end
                else:
                    min_ind = min(chars.values())
                    start = min_ind + 1
                    del chars[string[min_ind]]
            max_len = max(end - start + 1, max_len)
            end += 1
        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.longestsubstrtwodistinctchars('eceba'))
    print(s.longestsubstrtwodistinctchars('ccaabbb'))








