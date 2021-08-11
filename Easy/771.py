
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         num_stones = 0
#         jewels = list(jewels)
#         for jewel in jewels:
#             num_stones += stones.count(jewel)
            
#         return num_stones


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(jewel in list(jewels) for jewel in stones)

solution = Solution()
print(solution.numJewelsInStones('aA', 'aAAbbbb'))
