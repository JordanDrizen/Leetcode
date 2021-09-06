from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        interval = arr[1] - arr[0]
        return all(arr[i + 1] - arr[i] == interval for i in range(1, len(arr) - 1))


solution = Solution()
print(solution.canMakeArithmeticProgression([3, 5, 1]))
