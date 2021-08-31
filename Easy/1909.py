from typing import List


class Solution:
    def strictlyIncreasing(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False
        return True

    def canBeIncreasing(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums) and nums == sorted(nums):
            return True
        for i in range(len(nums)):
            if self.strictlyIncreasing(nums[:i] + nums[i+1:]):
                return True
        return False


solution = Solution()
print(solution.canBeIncreasing([1,1,1]))
# print(solution.strictlyIncreasing([1,1,1]))
