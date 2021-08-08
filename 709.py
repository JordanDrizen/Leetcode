class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            ans += chr(ord(s[i]) + 32) if 65 <= ord(s[i]) <= 90 else s[i]
        return ans


solution = Solution()
print(solution.toLowerCase("Hello"))
