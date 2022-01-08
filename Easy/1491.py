from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.pop(salary.index(max(salary)))
        salary.pop(salary.index(min(salary)))
        return sum(salary) / len(salary)


solution = Solution()
print(solution.average([4000, 3000, 1000, 2000]))
