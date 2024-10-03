# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=10000
        sell=0
        max_profit=0

        for price in prices:
            if price<buy:
                buy=price
            profit=price-buy
            if profit>max_profit:
                max_profit=profit

        return max_profit