from typing import List
from timeit import default_timer as timer


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


start = timer()
solution = Solution()
print(solution.getConcatenation([1, 2, 1]))
end = timer()
print((end - start) * 1000)
