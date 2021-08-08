from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [None] * len(s)
        for i in range(len(s)):
            ans[indices[i]] = s[i]
        ans = "".join(ans)
        return ans


solution = Solution()
print(solution.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
