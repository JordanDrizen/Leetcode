from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        nums = [str(num) for num in nums]
        for num in nums:
            ans += 1 if len(num) % 2 == 0 else 0
        return ans



solution = Solution()
print(solution.findNumbers([12,345,2,6,7896]))
