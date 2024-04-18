class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        part_sum = [0] * n
        part_sum[0] = nums[0]
        
        for i in range(1, n):
            part_sum[i] = part_sum[i - 1] + nums[i]
        
        for i in range(n):
            left_sum = part_sum[i]
            right_sum = part_sum[n - 1] - part_sum[i]
            result[i] = abs(left_sum - (nums[i] * (i + 1))) + abs(right_sum - (nums[i] * (n - i - 1)))
        
        return result
