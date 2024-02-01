class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, memo):
            if memo[i][j] != -1:
                return memo[i][j]
    
            longest_path = 1
    
            for di, dj in directions:
                ni, nj = i + di, j + dj
    
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    length = 1 + dfs(ni, nj, memo)
                    longest_path = max(longest_path, length)
    
            memo[i][j] = longest_path
            return longest_path
    
        memo = [[-1] * n for _ in range(m)]
    
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j, memo))
    
        return result