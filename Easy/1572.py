from typing import List


# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         sum = 0
#         for i in range(len(mat)):
#             sum += mat[i][i] + mat[i][len(mat) - 1 - i]
#             if i == len(mat) - 1 - i:
#                 sum -= mat[i][i]
#         return sum

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i]
            if i != len(mat) - 1 - i:
                sum += mat[i][len(mat) - 1 - i]
        return sum


solution = Solution()
print(solution.diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]))
