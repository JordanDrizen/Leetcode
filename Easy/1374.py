class Solution:
    def generateTheString(self, n: int) -> str:
        ans = ""
        if n % 2 == 0 :
            ans += 'w' * (n-1)
            ans += 'z'
        else:
            ans += 'w' * n
        return ans

solution = Solution()
print(solution.generateTheString(1))
