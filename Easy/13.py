class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        s = s[::-1]
        ans = 0
        i = 1
        while i < len(s):
            if numerals[s[i]] < numerals[s[i-1]]:
                ans += numerals[s[i-1]] - numerals[s[i]]
                i += 2
            else:
                if i == 1:
                    ans += numerals[s[i-1]]
                ans += numerals[s[i]]
                i += 1
        if len(s) <= 2:
            return ans
        if numerals[s[i-1]] < numerals[s[i-2]]:
            ans -= numerals[s[i-1]]
        else:
            pass
        return ans


solution = Solution()
print(solution.romanToInt("MCMXCIV"))
