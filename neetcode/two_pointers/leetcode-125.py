# Given a string s, return true if string is valid palindrome, or false
# othterwise

class Solution:
    def isPalindrome(self,s:str)->bool:
        import re
        regex = re.compile("\W")
        s = regex.sub("",s).replace("_","")
        print(s)
        if len(s) == 0: return True
        head,tail = 0,len(s)-1
        while head <= tail:
            if s[head].lower()!=s[tail].lower():
                return False
            head = head+1
            tail = tail-1
        return True

    def display(self,s):
        print(f"Output for input string {s}: {self.isPalindrome(s)}")


if __name__ == "__main__":
    s = Solution()
    input = "A man, a plan, a canal: Panama"
    s.display(input)
