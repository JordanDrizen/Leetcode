from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans


solution = Solution()
print(solution.shuffle([2, 5, 1, 3, 4, 7], 3))
