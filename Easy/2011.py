from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for op in operations:
            if op == "++X" or op == "X++":
                val += 1
            else:
                val -= 1
        return val


solution = Solution()
print(solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))
