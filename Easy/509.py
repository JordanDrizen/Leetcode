import math


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        fib_arr = [0, 1]
        for i in range(2, n + 1):
            fib_arr.append(fib_arr[i - 1] + fib_arr[i - 2])
        return fib_arr[-1]


# class Solution:
#     def fib(self, n: int) -> int:
#         fib_formula = (((1+math.sqrt(5))/2)**n)/math.sqrt(5)
#         return round(fib_formula)

solution = Solution()
print(solution.fib(0))
