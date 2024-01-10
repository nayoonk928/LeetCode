class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        visited = [0 for _ in range(len(nums))]

        def dfs(count, curr_list):
            if count == len(nums):
                answer.append(curr_list[:])
                return

            for idx, val in enumerate(nums):
                if visited[idx] == 1:
                    continue
        
                curr_list.append(val)
                visited[idx] = 1
        
                dfs(count + 1, curr_list)
                curr_list.pop()
                visited[idx] = 0
        
        dfs(0, [])
        return answer