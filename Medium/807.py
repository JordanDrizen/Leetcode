from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        south_view = []
        north_view = []
        west_view = [max(row) for row in grid]
        east_view = [max(row) for row in grid[::-1]]
        print("west", west_view)
        print("east", east_view)
        # for i in range(len(grid)):
        #     south_view.append(max([row[i] for row in grid]))
        #     north_view.append(max([row[-i] for row in grid]))
        print(south_view, north_view)
        return


solution = Solution()
print(
    solution.maxIncreaseKeepingSkyline(
        [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    )
)
