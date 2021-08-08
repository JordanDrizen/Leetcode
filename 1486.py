class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        ans = nums[0]
        for num in nums[1:]:
            ans ^= num
        return ans


solution = Solution()
print(solution.xorOperation(5, 0))
