class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        if 6 in nums:
            first_six = nums.index(6)
            nums[first_six] = 9
            nums = [str(x) for x in nums]
            return int(''.join(nums))
        return num


solution = Solution()
print(solution.maximum69Number(9669))
