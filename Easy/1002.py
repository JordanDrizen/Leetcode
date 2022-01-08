from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = set(words[0])
        for word in words[1:]:
            ans = set(word) & ans
        res = []
        for char in ans:
            minimum = 101
            for word in words:
                minimum = min(minimum, word.count(char))
            for _ in range(minimum):
                res.append(char)
        return res


solution = Solution()
print(solution.commonChars(["bella", "label", "roller"]))
