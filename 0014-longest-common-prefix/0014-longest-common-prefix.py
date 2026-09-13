class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            # Shrink the prefix until it matches the start of the current string
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                    
        return prefix