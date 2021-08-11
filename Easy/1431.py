from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [kid + extraCandies >= max_candy for kid in candies]


solution = Solution()
print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))
