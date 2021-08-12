from typing import List
import math


class Solution:
    def dist(self, p1: List[int], p2: List[int]) -> float:
        return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        num_points = []
        for circle in queries:
            center = [circle[0], circle[1]]
            radius = circle[2]
            count = 0
            for point in points:
                if self.dist(center, point) <= radius:
                    count += 1
            num_points.append(count)
        return num_points


solution = Solution()
print(
    solution.countPoints(
        [[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    )
)
