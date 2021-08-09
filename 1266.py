from typing import List
import math


# class Solution:

#     num_steps = 0
#     current_point = []

#     def distance(self, p1: List[int], p2: List[int]) -> float:
#         dist = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

#         return dist

#     def stepsToPoint(self, end_point: List[int]) -> int:
#         if self.current_point == end_point:
#             return self.num_steps
#         else:
#             self.num_steps += 1
#             if int(self.distance(self.current_point, end_point)) == 1:
#                 self.current_point = end_point
#             elif self.current_point[0] == end_point[0]:
#                 if self.current_point[1] < end_point[1]:
#                     self.current_point[1] += 1
#                 else:
#                     self.current_point[1] -= 1
#             elif self.current_point[1] == end_point[1]:
#                 if self.current_point[0] < end_point[0]:
#                     self.current_point[0] += 1
#                 else:
#                     self.current_point[0] -= 1
#             elif (
#                 self.current_point[0] > end_point[0]
#                 and self.current_point[1] > end_point[1]
#             ):
#                 self.current_point[0] -= 1
#                 self.current_point[1] -= 1
#             elif (
#                 self.current_point[0] < end_point[0]
#                 and self.current_point[1] < end_point[1]
#             ):
#                 self.current_point[0] += 1
#                 self.current_point[1] += 1
#             else:
#                 if self.current_point[0] < end_point[0]:
#                     self.current_point[0] += 1
#                 elif self.current_point[0] > end_point[0]:
#                     self.current_point[0] -= 1
#             self.stepsToPoint(end_point)

#     def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
#         self.current_point = points[0]
#         for i in range(1, len(points)):
#             self.stepsToPoint(points[i])
#         return self.num_steps


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        num_steps = 0
        current_point = points[0]
        for i in range(1, len(points)):
            num_steps += max(
                abs(points[i][0] - current_point[0]),
                abs(points[i][1] - current_point[1]),
            )
            current_point = points[i]
        return num_steps


solution = Solution()
print(solution.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
