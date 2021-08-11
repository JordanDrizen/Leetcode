from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = [None] * len(nums)
        for i in range(len(nums)):
            if ans[index[i]] == None:
                ans[index[i]] = nums[i]
            else:
                ans.insert(index[i], nums[i])
        ans = ans[: len(nums)]
        return ans


solution = Solution()
print(solution.createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))

# ls = [1, 2, 3, 4, 0]
# ls.insert(0, 5)
# print(ls)
