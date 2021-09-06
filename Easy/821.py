from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = [i for i in range(len(s)) if s[i] == c]
        ans = []
        for i in range(len(s)):
            dist = 10 ** 4
            for index in indices:
                dist = min(abs(i - index), dist)
            ans.append(dist)
        return ans


solution = Solution()
print(solution.shortestToChar("loveleetcode", "e"))
