# dp[0] = -2, dp[1] = -1/1 중에서 1 선택, dp[2] = -2/-3 중에서 -2 선택, dp[3] = 4/2 중에서 4 선택 ...
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        
        dp.append(nums[0])
        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
        
        dp.sort()
        
        return dp[-1]
        