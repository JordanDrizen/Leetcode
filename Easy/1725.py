from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        largest_squares = []
        for rectangle in rectangles:
            largest_squares.append(min(rectangle))
        return largest_squares.count(max(largest_squares))



solution = Solution()
print(solution.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))
