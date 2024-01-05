class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {} 
        max_length = 0  
        start = 0  

        for index, ch in enumerate(s):
            if ch in used and start <= used[ch]:
                start = used[ch] + 1
            else:
                max_length = max(max_length, index - start + 1)  

            used[ch] = index
        return max_length
