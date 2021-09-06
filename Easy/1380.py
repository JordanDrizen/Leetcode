from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_rows = []
        max_cols = []
        for i in range(len(matrix)):
            min_rows.append(min(matrix[i]))
        cols = list(zip(*matrix))
        for i in range(len(cols)):
            max_cols.append(max(cols[i]))
        return [val for val in min_rows if val in set(max_cols)]


solution = Solution()
print(solution.luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
