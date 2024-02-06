class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        strs.sort()
        
        first_str = strs[0]
        last_str = strs[-1]
        
        for i, char in enumerate(first_str):
            if char != last_str[i]:
                return first_str[:i]
        
        return first_str
        
        