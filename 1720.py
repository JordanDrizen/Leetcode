from typing import List


# class Solution:
#     def decode(self, encoded: List[int], first: int) -> List[int]:
#         ans = [first]
#         for num in encoded:
#             ans.append(num ^ first)
#             first = num^first
#         return ans


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for num in encoded:
            ans.append(ans[-1] ^ num)
        return ans


solution = Solution()
print(solution.decode([1, 2, 3], 1))
