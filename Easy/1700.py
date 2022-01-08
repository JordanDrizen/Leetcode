from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while (0 in students and 0 in sandwiches) or (
            1 in students and 1 in sandwiches
        ):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students = students[1:] + [students[0]]
            print(students, sandwiches)
        return len(students)


solution = Solution()
print(solution.countStudents([1, 1, 1, 0], [1, 0, 0, 0]))
