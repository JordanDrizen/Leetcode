from typing import List
import math


# class Solution:

#     num_steps = 0
#     current_point = []

#     def stepsToPoint(self, p1: List[int], p2: List[int]) -> int:
#         if p1 == p2:
#             return 0
#         else:
#             if p1[0] == p1[1] and p2[0] == p2[1]:
#                 return abs(p1[0] - p2[0])
#             elif p1[0] == p2[0]:
#                 return abs(p1[1] - p2[1])
#             elif p1[1] == p2[1]:
#                 return abs(p1[0] - p2[0])
#             else:
#                 if p1[0] < p2[0]:
#                     self.stepsToPoint(p1[0] + 1)
#         return

#     def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
#         self.current_point = [3,4]
#         for i in range(len(points)-1):
#             if self.current_point == points[i+1]:
#                 return self.num_steps
#             else:
#                 if self.current_point[0] == self.current_point[1] and points[i+1][0] == points[i+1][1]:
#                     self.num_steps += abs(points[i][0] - points[i+1][0])
#                     self.current_point = points[i+1]
#                 else:
#                     if self.current_point[0] == points[i+1][0]:
#                         self.num_steps += abs(self.current_point[1] - points[i+1][1])
#                         self.current_point = points[i+1]
#                     elif self.current_point[1] == points[i+1][1]:
#                         self.num_steps += abs(self.current_point[0] - points[i+1][0])
#                         self.current_point = points[i+1]
#         return


class Solution:

    num_steps = 0
    current_point = []

    def distance(self, p1: List[int], p2: List[int]) -> float:
        dist = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

        return dist

    def stepsToPoint(self, end_point: List[int]) -> int:
        if self.current_point == end_point:
            return self.num_steps
        else:
            self.num_steps += 1
            if int(self.distance(self.current_point, end_point)) == 1:
                self.current_point = end_point
            elif self.current_point[0] == end_point[0]:
                if self.current_point[1] < end_point[1]:
                    self.current_point[1] += 1
                else:
                    self.current_point[1] -= 1
            elif self.current_point[1] == end_point[1]:
                if self.current_point[0] < end_point[0]:
                    self.current_point[0] += 1
                else:
                    self.current_point[0] -= 1
            elif (
                self.current_point[0] > end_point[0]
                and self.current_point[1] > end_point[1]
            ):
                self.current_point[0] -= 1
                self.current_point[1] -= 1
            elif (
                self.current_point[0] < end_point[0]
                and self.current_point[1] < end_point[1]
            ):
                self.current_point[0] += 1
                self.current_point[1] += 1
            else:
                if self.current_point[0] < end_point[0]:
                    self.current_point[0] += 1
                elif self.current_point[0] > end_point[0]:
                    self.current_point[0] -= 1
            self.stepsToPoint(end_point)

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        self.current_point = points[0]
        for i in range(1, len(points)):
            self.stepsToPoint(points[i])
        return self.num_steps


solution = Solution()
print(solution.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
# print(solution.distance([1,1], [2,1]))
