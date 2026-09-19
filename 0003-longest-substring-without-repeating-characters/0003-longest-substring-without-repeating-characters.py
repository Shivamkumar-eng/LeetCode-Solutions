class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        d={}
        max_length=0
        for right in range(len(s)):
            if s[right] in d and d[s[right]]>=left:
                left=d[s[right]]+1
            d[s[right]]=right
            current_length=right-left+1
            if current_length>=max_length:
                max_length=current_length
        return max_length