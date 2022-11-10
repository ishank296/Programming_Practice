# increasing triplet subsequence
# check if there exists triplet i,j,k such that
# i < j < k and a[i] < a[j] < a[k]

class Solution:

    def checkincreasingtripletsubseq(self,nums: list[int]) -> bool:
        num1 = float('inf')
        num2 = float('inf')
        for num in nums:
            if num < num1:
                num1 = num
            elif num < num2:
                num2 = num
            else:
                return True
        return False


if __name__ == "__main__":
    numlist1 = [1,2,3,4,5]
    numlist2 = [5,4,2,3,1]
    numlist3 = [2,1,5,0,4,6]
    s = Solution()
    print(s.checkincreasingtripletsubseq(numlist1))
    print(s.checkincreasingtripletsubseq(numlist2))
    print(s.checkincreasingtripletsubseq(numlist3))