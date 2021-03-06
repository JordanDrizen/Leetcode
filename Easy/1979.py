from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(nums[0], 0, -1):
            if nums[-1] % i == 0 and nums[0] % i == 0:
                return i


solution = Solution()
print(solution.findGCD([2, 5, 6, 9, 10]))
