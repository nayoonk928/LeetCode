class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()  
        max_length = 0  
        start = 0  

        for index, ch in enumerate(s):
            while ch in chars:
                chars.remove(s[start])  
                start += 1  
            chars.add(ch)  
            max_length = max(max_length, index - start + 1)  

        return max_length
