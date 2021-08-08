class Solution:
    def lastLetter(self, s: str) -> int:
        return s[-1]

    def sortSentence(self, s: str) -> str:
        ans = s.split()
        ans.sort(key=self.lastLetter)
        ans = [word[:-1] for word in ans]
        ans = " ".join(ans)
        return ans


solution = Solution()
print(solution.sortSentence("is2 sentence4 This1 a3"))
