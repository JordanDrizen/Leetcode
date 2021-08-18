class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        for word in s.split():
            ans += word[::-1] + " "
        return ans[:-1]


solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))
