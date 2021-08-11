from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, int(n/2)+1):
            ans.append(i)
            ans.append(-i)
        if n % 2 == 1:
            ans.append(0)
        return ans

solution = Solution()
print(solution.sumZero(1))
