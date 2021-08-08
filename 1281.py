class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = list(str(n))
        product = 1
        sum = 0
        for i in num:
            product *= int(i)
            sum += int(i)
        return product - sum


solution = Solution()
print(solution.subtractProductAndSum(234))
