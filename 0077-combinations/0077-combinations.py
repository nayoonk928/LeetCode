class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        
        def dfs(idx, curr_list):
            if len(curr_list) == k:
                answer.append(curr_list[:])
                return
            
            for i in range(idx, n + 1):
                dfs(i + 1, curr_list + [i])
        
        dfs(1, [])
        return answer