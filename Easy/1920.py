from typing import List
from timeit import default_timer as timer


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            ans.append(nums[nums[i]])
        return ans


start = timer()
solution = Solution()
print(solution.buildArray(nums=[3, 0, 1, 2]))
end = timer()
print((end - start) * 1000)
