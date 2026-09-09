class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        d={}
        max_length=0
        for right,char in enumerate(s):
            if char in d and d[char]>=left:
                left=d[char]+1
            d[char]=right
            current_length=right-left+1
            if current_length>=max_length:
                max_length=current_length
        return max_length