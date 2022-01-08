
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        while target in nums:
            ans.append(nums.index(target))
            nums[nums.index(target)] = None
        return ans


solution = Solution()
print(solution.targetIndices([1, 2, 5, 2, 3], 2))
