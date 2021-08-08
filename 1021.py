# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         arr = []
#         sub = ""
#         num_left = 0
#         num_right = 0
#         for i in range(len(s)):
#             if s[i] == "(":
#                 num_left += 1
#                 sub += "("
#             elif s[i] == ")":
#                 num_right += 1
#                 sub += ")"
#             if num_left == num_right:
#                 num_left = 0
#                 num_right = 0
#                 sub = sub[1:]
#                 sub = sub[:-1]
#                 arr.append(sub)
#                 sub = ""
#         return "".first_leftoin(arr)


# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         ans = ""
#         sub = ""
#         counter = {}
#         for i in range(len(s)):
#             counter[s[i]] = counter.get(s[i], 0) + 1
#             sub += s[i]
#             if ")" in counter and counter["("] == counter[")"]:
#                 ans += sub[1:-1]
#                 sub = ""
#         return ans


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        num_left = 0
        num_right = 0
        first_left = 0
        for i in range(len(s)):
            if s[i] == "(":
                num_left += 1
            elif s[i] == ")":
                num_right += 1
            if num_left == num_right:
                ans += s[first_left + 1 : i]
                first_left = i + 1
        return ans


solution = Solution()
print(solution.removeOuterParentheses("(()())(())"))
