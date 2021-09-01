import math

class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(0, math.ceil(x/2) + 1):
            if i*i == x or i*i < x < (i+1)*(i+1):
                return i

solution = Solution()
print(solution.mySqrt(0))
