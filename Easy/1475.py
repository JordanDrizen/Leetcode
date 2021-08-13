from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discounts = []
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discounts.append(prices[i] - prices[j])
                    break
            if len(discounts) != i + 1:
                discounts.append(prices[i])
        discounts.append(prices[-1])
        return discounts


solution = Solution()
print(solution.finalPrices([8, 4, 6, 2, 3]))

# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         discounts = []

#         for i in range(len(prices) - 1):
#             vals_less = [val for val in prices[i + 1 :] if val <= prices[i]]
#             if vals_less:
#                 discounts.append(prices[i] - prices[prices.index(vals_less[0])])
#             else:
#                 discounts.append(prices[i])
#         discounts.append(prices[-1])
#         return discounts
