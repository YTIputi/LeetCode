class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x >= 0 and str(x) == str(x)[::-1]

s = Solution()
print(s.isPalindrome(0))