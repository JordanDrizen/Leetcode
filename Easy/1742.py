class Solution:
    def sumDigits(self, num: int) -> int:
        return sum(int(digit) for digit in str(num))

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        num_balls = [0] * 46
        for i in range(lowLimit, highLimit + 1):
            sum = self.sumDigits(i)
            num_balls[sum] += 1
        return max(num_balls)


solution = Solution()
print(solution.countBalls(10, 20))
