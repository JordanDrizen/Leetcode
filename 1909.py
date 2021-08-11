from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        print(len(set(nums)))
        if len(set(nums)) == len(nums) and nums == sorted(nums):
            return True
        for i in range(1, len(nums)-1):
            if nums[i] <= nums[i-1]
        return


solution = Solution()
print(solution.canBeIncreasing([1,2,10,5,7]))
