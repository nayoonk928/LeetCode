class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        
        left = 0
        right = len(height) - 1
        
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            answer = max(answer, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return answer
            