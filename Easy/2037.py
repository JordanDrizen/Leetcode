from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves = 0
        students.sort()
        seats.sort()
        for seat, student in zip(seats, students):
            moves += abs(seat - student)
        return moves


solution = Solution()
print(solution.minMovesToSeat([3, 1, 5], [2, 7, 4]))
