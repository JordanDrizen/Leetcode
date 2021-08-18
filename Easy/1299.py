from typing import List


# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         ans = []
#         for i in range(len(arr) - 1):
#             ans.append(max(arr[i+1:]))
#         return ans + [-1]


# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         return [max(arr[i+1:]) for i in range(len(arr)-1)] + [-1]


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        ans = []
        for i in range(1, len(arr) - 1):
            ans.append(max(arr[i + 1 :]))
        return [max(arr)] + ans + [-1]


solution = Solution()
print(solution.replaceElements([17, 18, 5, 4, 6, 1]))
