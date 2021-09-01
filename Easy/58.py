class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
