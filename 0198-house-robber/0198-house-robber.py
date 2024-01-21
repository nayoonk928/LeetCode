# 두 인접한 집들이 같은 날 도둑맞으면 경찰에 자동 연락감
# 하루에 경찰 출동 없이 훔칠 수 있는 가장 많은 돈 반환
# dp[0] = 0, dp[1] = 1, dp[2] = dp[0] + nums[1] 과 dp[1] 중 큰 것 
class Solution:
    def rob(self, nums: List[int]) -> int:        
        n = len(nums)
        
        if n == 1: 
            return nums[0]
        
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        
        for i in range(1, n):
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])
            
        return dp[n]
        