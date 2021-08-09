from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                ans += abs((nums[i] - nums[i - 1])) + 1
                nums[i] += abs((nums[i] - nums[i - 1])) + 1
        return ans


solution = Solution()
print(solution.minOperations([7, 6, 1, 9, 9, 10]))
