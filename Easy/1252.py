from typing import List


# class Solution:
#     def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
#         arr = [[0] * n] * m
#         for index in indices:
#             arr[index[0]] = [num + 1 for num in arr[index[0]]]
#             for i in range(m):
#                 arr[i][index[1]] += 1
#         print(arr)
#         sol = []
#         for nums in arr:
#             sol.append(list(map(lambda x: True if x % 2 != 0 else False, nums)))
#         ans = 0
#         for vals in sol:
#             ans += vals.count(True)
#         return ans


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        arr = [[0] * n for _ in range(m)]
        for row, col in indices:
            for j in range(n):
                arr[row][j] += 1
            for i in range(m):
                arr[i][col] += 1
        sol = []
        for nums in arr:
            sol.append(list(map(lambda x: True if x % 2 != 0 else False, nums)))
        ans = 0
        for vals in sol:
            ans += vals.count(True)

        return ans


solution = Solution()
print(solution.oddCells(2, 3, [[0, 1], [1, 1]]))
