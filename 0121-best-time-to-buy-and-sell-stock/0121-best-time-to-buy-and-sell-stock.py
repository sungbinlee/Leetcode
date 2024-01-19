class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')  # 무한대로 초기화

        for price in prices:
            min_price = min(min_price, price)  # 최솟값 갱신
            max_profit = max(max_profit, price - min_price)  # 최대 이익 갱신
    
        return max_profit