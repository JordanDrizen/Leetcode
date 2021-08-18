from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        if expected == heights:
            return 0
        ans = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
        return ans


solution = Solution()
print(solution.heightChecker([1, 1, 4, 2, 1, 3]))
