from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in accounts:
            if wealth < sum(i):
                wealth = sum(i)
        return wealth


solution = Solution()
print(solution.maximumWealth([[1, 2, 3], [3, 2, 1]]))
