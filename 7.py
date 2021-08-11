class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        ans = ""
        if x[0] == '-':
            ans += '-'
            ans += x[:0:-1]
            while ans[1] == '0':
                ans = ans[0] + ans[2:]
        else:
            ans += x[::-1]
            while ans[0] == '0' and len(ans) > 1:
                ans = ans[1:]
        if int(ans) < -2 ** 31  or int(ans) > (2 ** 31) - 1:
            ans = 0
        return int(ans)


solution = Solution()
print(solution.reverse(
1534236469))
