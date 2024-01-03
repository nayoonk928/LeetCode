class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in result:
                return [i, result[complement]]
            else:
                result[num] = i
        