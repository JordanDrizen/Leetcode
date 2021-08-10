from typing import List




class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # lists = [[]]
        # sum = 0
        # for i in range(len(nums) + 1):
        #     for j in range(i):
        #         lists.append(nums[j: i])
        # for l in lists:
        #     xor = 0
        #     for num in l:
        #         xor ^= num
        #         print(l, xor)
        #     sum += xor
        # return sum


solution = Solution()
print(solution.subsetXORSum([5,1,6]))
