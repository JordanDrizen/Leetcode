class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = 0
        num_hash = s.count('#')
        while i < len(s):
            if num_hash > 0:
                if s[i+2] == '#':
                    ans += chr(int(s[i] + s[i+1]) + 96)
                    num_hash -= 1
                    i += 3
                else:
                    ans += chr(int(s[i]) + 96)
                    i += 1
            else:
                ans += chr(int(s[i]) + 96)
                i += 1
        return ans


solution = Solution()
print(solution.freqAlphabets("10#11#12"))
