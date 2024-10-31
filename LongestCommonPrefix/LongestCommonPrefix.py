from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            prefix = self.findPrefix(prefix, word)
            if not prefix:
                return prefix
        return prefix
    
    def findPrefix(self, s1: str, s2: str) -> str:
        prefix = ""
        s1Lengh, s2Lengh = len(s1), len(s2)
        for i in range(s1Lengh):
            if i < s2Lengh and s1[i] == s2[i]:
                prefix += s1[i]
            else:
                return prefix
        return prefix
            

s = Solution()
print(s.longestCommonPrefix(["dog","racecar","car"]))