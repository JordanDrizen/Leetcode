from typing import List
from timeit import default_timer as timer


# #Slow 56 ms
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in range(len(nums)):
#             ans.append(sum(nums[:i+1]))
#         return ans


# solution = Solution()
# print(solution.runningSum([1, 2, 3, 4]))

# 40 ms
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        ans = []
        for i in range(len(nums)):
            ans.append(sum + nums[i])
            sum += nums[i]
        return ans


solution = Solution()
start = timer()
print(solution.runningSum([1, 2, 3, 4]))
end = timer()
print((end - start) * 1000)
