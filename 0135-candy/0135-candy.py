class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # 왼쪽에서 오른쪽으로 이동하면서 캔디 수 결정
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                
        # 오른쪽에서 왼쪽으로 이동하면서 캔디 수 업데이트
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # 모든 캔디 수 더하기
        return sum(candies)