from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if prices == list(reversed(sorted(prices))):
#             return 0
#         max_profit = 0
#         for i in range(len(prices) - 1):
#             if any(price > prices[i] for price in prices[i + 1 :]):
#                 max_profit = max((max(prices[i + 1 :]) - prices[i]), max_profit)
#         return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit = max((max(prices[i + 1 :]) - prices[i]), max_profit)
        return max_profit


solution = Solution()
print(solution.maxProfit([7, 6, 4, 3, 1]))
