class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        visited = [0 for _ in range(len(nums))]

        def dfs(count, elements):
            if count == len(nums):
                answer.append(elements[:])
                return

            for idx, val in enumerate(nums):
                if visited[idx] == 1:
                    continue
        
                elements.append(val)
                visited[idx] = 1
        
                dfs(count + 1, elements)
                elements.pop()
                visited[idx] = 0
        
        dfs(0, [])
        return answer