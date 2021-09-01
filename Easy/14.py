from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(len(word) for word in strs)
        for i in range(0, shortest_word+1):
            prefix = strs[0][0:i+1]
            for word in strs:
                if word[0:i+1] != prefix:
                    return prefix[0:i]
        return prefix

solution = Solution()
print(solution.longestCommonPrefix([""]))
