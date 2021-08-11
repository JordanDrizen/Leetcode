from typing import List


# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         max_1 = max(nums)
#         nums.remove(max_1)
#         max_2 = max(nums)
#         return (max_1 - 1) * (max_2 - 1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return (nums[-1] - 1) * (nums[-2] - 1)

solution = Solution()
print(solution.maxProduct([3,4,5,2]))
