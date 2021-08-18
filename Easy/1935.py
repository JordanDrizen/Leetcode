class Solution:
    def charInWord(self, s: str, broken: str) -> bool:
        for char in broken:
            if char in s:
                return True
        return False

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        for word in text.split():
            if not self.charInWord(word, brokenLetters):
                ans += 1
        return ans


solution = Solution()
print(solution.canBeTypedWords("hello world", "ad"))
