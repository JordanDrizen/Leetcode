from typing import List
from itertools import combinations


# class Solution:
#     def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
#         ans = []
#         for i in combinations(arr, 3):
#             ans.append(i)
#         sol = 0
#         for i in range(len(ans)):
#             if (
#                 abs(ans[i][0] - ans[i][1]) <= a
#                 and abs(ans[i][1] - ans[i][2]) <= b
#                 and abs(ans[i][0] - ans[i][2]) <= c
#             ):
#                 sol += 1
#         return sol


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if (
                        abs(arr[i] - arr[j]) <= a
                        and abs(arr[j] - arr[k]) <= b
                        and abs(arr[i] - arr[k]) <= c
                    ):
                        ans += 1
        return ans


solution = Solution()
print(solution.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3))
