class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping = {}
        mapped_chars = set()
        
        for char_s, char_t in zip(s, t):
            if char_s not in mapping:
                if char_t in mapped_chars:
                    return False
                mapping[char_s] = char_t
                mapped_chars.add(char_t)
            elif mapping[char_s] != char_t:
                return False
        
        return True