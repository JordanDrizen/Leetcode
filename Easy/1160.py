from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_length = 0
        for word in words:
            good_word = True
            for char in word:
                if word.count(char) > chars.count(char) or char not in chars:
                    good_word = False
                    break
            if good_word:
                total_length += len(word)
        return total_length


solution = Solution()
print(solution.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
