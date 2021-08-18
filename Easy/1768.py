class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1 = len(word1)
        len_2 = len(word2)
        min_len = min(len_1, len_2)
        ans = ""
        for i in range(min_len):
            ans += word1[i] + word2[i]
        return ans + word1[i + 1 :] + word2[i + 1 :]


solution = Solution()
print(solution.mergeAlternately("ab", "pqrs"))
