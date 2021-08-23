from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return max(nums)
        return nums[-3]


solution = Solution()
print(solution.thirdMax([-1, 2, 3]))
