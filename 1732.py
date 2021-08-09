from typing import List


# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         ans = [0]
#         for i in range(len(gain)):
#             ans.append(ans[i] + gain[i])
#         return max(ans)


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        alt = 0
        for i in range(len(gain)):
            alt += gain[i]
            ans = max(ans, alt)
        return ans


solution = Solution()
print(solution.largestAltitude([-5, 1, 5, 0, -7]))
