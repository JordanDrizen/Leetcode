class Solution:
    def replaceDigits(self, s: str) -> str:
        s = [char for char in s]
        for i in range(1, len(s), 2):
            s[i] = chr(ord(s[i - 1]) + int(s[i]))
        return "".join(s)


solution = Solution()
print(solution.replaceDigits("a1c1e1"))
