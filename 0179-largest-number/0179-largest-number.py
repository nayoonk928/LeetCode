class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return str(x) + str(y) < str(y) + str(x)
    
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and compare(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1
        
        result = ''.join(map(str, nums))
        return str(int(result)) if int(result) != 0 else "0"
        