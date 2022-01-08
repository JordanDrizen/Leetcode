
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        arr = []
        for sentence in sentences:
            arr.append(len(sentence.split()))
        return max(arr)


solution = Solution()
print(solution.mostWordsFound(
    ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
