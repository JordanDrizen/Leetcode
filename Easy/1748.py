from typing import List


# class Solution:
#     def sumOfUnique(self, nums: List[int]) -> int:
#         counter = {}
#         ans = 0
#         for num in nums:
#             counter[num] = counter.get(num, 0) + 1
#         for key in counter:
#             if counter[key] == 1:
#                 ans += key
#         return ans


# class Solution:
#     def sumOfUnique(self, nums: List[int]) -> int:
#         counter = {}
#         for num in nums:
#             if counter.get(num) == None or counter.get(num) == 0:
#                 counter[num] = counter.get(num, 1)
#             else:
#                 counter[num] = counter.get(num) - 1
#         return sum(key for key in counter.keys() if counter[key] != 0)


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = num
            else:
                counter[num] = 0
        return sum(counter.values())


solution = Solution()
print(solution.sumOfUnique([1, 1, 1, 1, 1]))
