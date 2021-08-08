from typing import List


# class Solution:
#     def maxProductDifference(self, nums: List[int]) -> int:
#         ans = []
#         for _ in range(2):
#             ans.append(min(nums))
#             ans.append(max(nums))
#             nums.remove(min(nums))
#             nums.remove(max(nums))
#         ans.sort()
#         return (ans[-1] * ans[-2]) - (ans[0] * ans[1])


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


solution = Solution()
print(solution.maxProductDifference([5, 6, 2, 7, 4]))
