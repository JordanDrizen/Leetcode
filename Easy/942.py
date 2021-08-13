from typing import List


# class Solution:
#     def diStringMatch(self, s: str) -> List[int]:
#         nums = list(range(len(s) + 1))
#         if "I" not in s:
#             return nums[::-1]
#         elif "D" not in s:
#             return nums
#         else:
#             ans = []
#             for char in s:
#                 if char == "I":
#                     ans.append(nums[0])
#                     nums = nums[1:]
#                 else:
#                     ans.append(nums[-1])
#                     nums = nums[:-1]
#             return ans + [nums[0]]


# class Solution:
#     def diStringMatch(self, s: str) -> List[int]:
#         nums = list(range(len(s) + 1))
#         ans = []
#         for char in s:
#             if char == "I":
#                 ans.append(nums[0])
#                 nums = nums[1:]
#             else:
#                 ans.append(nums[-1])
#                 nums = nums[:-1]
#         return ans + [nums[0]]


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        max = len(s)
        min = 0
        ans = [0] * max
        for i in range(max):
            if s[i] == "I":
                ans[i] = min
                min += 1
            else:
                ans[i] = max
                max -= 1
        return ans + [min]


solution = Solution()
print(solution.diStringMatch("IDID"))
