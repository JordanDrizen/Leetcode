class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = {}
        for letter in s:
            counter[letter] = counter.get(letter, 0) + 1
        nums = sorted(counter.values())
        return nums[-1] == nums[0]



solution = Solution()
print(solution.areOccurrencesEqual("abacbc"))
