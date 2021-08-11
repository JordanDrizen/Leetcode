from typing import List


# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in range(len(nums)):
#             count = 0
#             for j in range(len(nums)):
#                 if nums[i] > nums[j]:
#                     count += 1
#             ans.append(count)
#         return ans


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            nums = sorted(nums)
            ans.append(nums.index(num))
        return ans


solution = Solution()
print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
