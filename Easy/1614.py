class Solution:
    def maxDepth(self, s: str) -> int:
        if "(" in s and ")" in s:
            max_depth = 0
            num_left = 0
            num_right = 0
            for i in range(len(s)):
                if s[i] == "(":
                    num_left += 1
                elif s[i] == ")":
                    num_right += 1
                if max_depth < num_left - num_right:
                    max_depth = num_left - num_right
            return max_depth
        else:
            return 0


solution = Solution()
print(solution.maxDepth("()"))
