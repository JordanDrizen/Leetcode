from typing import List


# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         ans = 0
#         for _ in range(len(nums)//2):
#             pair = []
#             pair.append(max(nums))
#             nums.pop(nums.index(max(nums)))
#             pair.append(max(nums))
#             nums.pop(nums.index(max(nums)))
#             ans += min(pair)
#         return ans


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans


solution = Solution()
print(solution.arrayPairSum([1, 4, 3, 2]))
