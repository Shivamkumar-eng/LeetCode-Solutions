class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        for i in range(len(s)):
            reverse=26-(ord(s[i])-ord('a'))
            sum+=(i+1)*reverse
        return sum