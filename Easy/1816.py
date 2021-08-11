# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         s = s.split()
#         ans = " ".join(s[:k])
#         return ans


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        ans = ""
        for i in range(k - 1):
            ans += s[i] + " "
        return ans + s[k - 1]


solution = Solution()
print(solution.truncateSentence("Hello how are you Contestant", 4))
