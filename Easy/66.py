from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(digit) for digit in digits]
        num = ''.join(digits)
        return [int(digit) for digit in str(int(num)+1)]

solution = Solution()
print(solution.plusOne([3, 0, 1, 2]))
