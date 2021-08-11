class Solution:
    ans = 0

    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return int(self.ans)
        else:
            if n % 2 == 0:
                self.ans += n / 2
                return self.numberOfMatches(n / 2)
            else:
                self.ans += (n - 1) / 2
                return self.numberOfMatches(((n - 1) / 2) + 1)


solution = Solution()
print(solution.numberOfMatches(14))
