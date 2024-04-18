class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]  # 최소 가격을 첫 번째 날의 주가로 설정
        max_profit = 0  # 최대 이익을 0으로 초기화
        
        # 각 날의 주가를 순회하면서 최소 가격과 최대 이익을 업데이트
        for price in prices:
            min_price = min(min_price, price)  # 최소 가격 갱신
            max_profit = max(max_profit, price - min_price)  # 최대 이익 갱신
        
        return max_profit
