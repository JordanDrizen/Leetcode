from typing import List


# class Solution:
#     def repeatedNTimes(self, nums: List[int]) -> int:
#         counter = {}
#         for num in nums:
#             if num in counter:
#                 return num
#             counter[num] = 1


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = []
        for num in nums:
            if num in counter:
                return num
            counter.append(num)


solution = Solution()
print(solution.repeatedNTimes([1, 2, 3, 3]))
