# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         s = s.lower()
#         num_1 = 0
#         num_2 = 0
#         for i in range(int(len(s)/2)):
#             if ord(s[i]) == 97 or ord(s[i]) == 101 or ord(s[i]) == 105 or ord(s[i]) == 111 or ord(s[i]) == 117:
#                 num_1 += 1
#             if ord(s[i + int(len(s)/2)]) == 97 or ord(s[i + int(len(s)/2)]) == 101 or ord(s[i + int(len(s)/2)]) == 105 or ord(s[i + int(len(s)/2)]) == 111 or ord(s[i + int(len(s)/2)]) == 117:
#                 num_2 += 1
#         return num_1 == num_2


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = ['a', 'e', 'i', 'o', 'u']
        num_1 = 0
        num_2 = 0
        for i in range(int(len(s)/2)):
            if s[i] in vowels:
                num_1 += 1
            if s[i + int(len(s)/2)] in vowels:
                num_2 += 1
        return num_1 == num_2


solution = Solution()
print(solution.halvesAreAlike("book"))
