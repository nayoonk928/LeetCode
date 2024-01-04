class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()  
        max_length = 0  
        left = 0  

        for right, ch in enumerate(s):
            while ch in chars:
                chars.remove(s[left])  
                left += 1  
            chars.add(ch)  
            max_length = max(max_length, right - left + 1)  

        return max_length
