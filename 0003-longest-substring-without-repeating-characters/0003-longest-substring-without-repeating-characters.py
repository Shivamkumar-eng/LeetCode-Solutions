class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        seen = {}

        for right in range(len(s)):

            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1

            seen[s[right]] = right

            length = right - left + 1

            if length > ans:
                ans = length

        return ans