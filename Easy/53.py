from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = -10 ** 5
        for i in range(len(nums)+1):
            for j in range(i):
                if sum(nums[j:i]) > max:
                    max = sum(nums[j:i])
                    print(nums[j:i])
        return max

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
