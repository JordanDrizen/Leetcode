from typing import List


# class Solution:

#     def binarySearch(self, arr: List[int], num: int) -> int:
#         low = 0
#         high = len(arr) - 1
#         mid = 0
#         while low <= high:
#             mid = (low + high) // 2
#             if arr[mid] > num:
#                 low = mid + 1
#             elif arr[mid] < num:
#                 high = mid - 1
#             else:
#                 return mid
#         return -1

#     def countNegatives(self, grid: List[List[int]]) -> int:
#         for arr in grid:
#             print(arr)
#             print(self.binarySearch(arr, -1))
#         return


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        num_neg = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    num_neg += len(grid[i]) - j
                    break
        return num_neg


solution = Solution()
print(
    solution.countNegatives(
        [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    )
)
