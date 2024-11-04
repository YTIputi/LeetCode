class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first = 0
        word = ''
        mx = 0
        for i in range(len(s)):
            if s[i] not in word:
                word += s[i]
            else:
                mx = max(mx, i - first)
                first += word.index(s[i]) + 1
                word = s[first: i + 1]
        return max(mx, len(word))

s = Solution()
print(s.lengthOfLongestSubstring('pwwkew'))