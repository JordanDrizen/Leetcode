from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = len(words)
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    ans -= 1
                    break
        return ans


solution = Solution()
print(solution.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
