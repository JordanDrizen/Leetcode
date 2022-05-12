# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         return s == s[::-1]

#     def validPalindrome(self, s: str) -> bool:
#         if self.isPalindrome(s):
#             return True
#         for i in range(len(s)):
#             if self.isPalindrome(s[0:i] + s[i+1:]):
#                 return True
#         return False

# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         if s == s[::-1]:
#             return True
#         reversed = s[::-1]
#         for i in range(len(s)//2):
#             if s[i] != reversed[i]:
#                 temp = s[0:i] + s[i+1:]
#                 temp_reversed = temp[::-1]
#                 temp_2 = reversed[0:i] + reversed[i+1:]
#                 temp_2_reversed = temp_2[::-1]
#                 if temp == temp_reversed or temp_2 == temp_2_reversed:
#                     return True
#         return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        arr = [char for char in s]
        left = 0
        right = len(arr) - 1
        while left < right:
            temp = arr.copy()
            temp.pop(left)
            if not self.isPalindrome(temp):
                left += 1
            else:
                return True
            temp = arr.copy()
            temp.pop(right)
            if not self.isPalindrome(temp):
                right -= 1
            else:
                return True
        return False

solution = Solution()
print(solution.validPalindrome("abc"))
