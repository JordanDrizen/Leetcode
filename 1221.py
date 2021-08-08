class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_r = 0
        num_l = 0
        ans = 0
        for letter in s:
            if letter == "R" and num_r + 1 != num_l:
                num_r += 1
            elif letter == "R" and num_r + 1 == num_l:
                num_r = 0
                num_l = 0
                ans += 1
            elif letter == "L" and num_l + 1 != num_r:
                num_l += 1
            elif letter == "L" and num_l + 1 == num_r:
                num_r = 0
                num_l = 0
                ans += 1
        return ans


solution = Solution()
print(solution.balancedStringSplit("RLRRRLLRLL"))
