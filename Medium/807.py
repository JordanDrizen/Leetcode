from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        cols = []
        for i in range(len(grid)):
            cols.append([row[i] for row in grid])
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == max(grid[i]) or grid[i][j] == max(cols[j]):
                    ans += 0
                else:
                    ans += min(max(grid[i]), max(cols[j])) - grid[i][j]
        return ans


solution = Solution()
print(
    solution.maxIncreaseKeepingSkyline(
        [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    )
)
