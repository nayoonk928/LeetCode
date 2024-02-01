class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:  
            return 0
    
        jumps = 0  # 최소 점프 횟수
        current_max_reach = 0  # 현재까지의 최대 도달 가능한 인덱스
        next_max_reach = 0  # 다음에 도달 가능한 최대 인덱스
    
        for i in range(n - 1):
            next_max_reach = max(next_max_reach, i + nums[i])
    
            if i == current_max_reach:
                jumps += 1
                current_max_reach = next_max_reach
    
        return jumps