
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # If lengths don't match, bijection is impossible
        if len(pattern) != len(words):
            return False
            
        char_to_word = {}
        word_to_char = {}
        
        for c, w in zip(pattern, words):
            # Check for mapping conflicts
            if (c in char_to_word and char_to_word[c] != w) or \
               (w in word_to_char and word_to_char[w] != c):
                return False
                
            # Establish the mapping
            char_to_word[c] = w
            word_to_char[w] = c
            
        return True