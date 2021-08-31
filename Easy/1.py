from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp_arr = nums[:i] + nums[i+1:]
            if target - nums[i] in temp_arr:
                return [i, temp_arr.index(target-nums[i]) + 1]


solution = Solution()
print(solution.twoSum([3,3], 6))
