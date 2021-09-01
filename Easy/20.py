class Solution:
    def isValid(self, s: str) -> bool:
        matching = ["()", "[]", "{}"]
        while any(chars in s for chars in matching):
            pair = matching[list(chars in s for chars in matching).index(True)]
            s = s[:s.index(pair)] + s[s.index(pair)+2:]
        return s == ""
        


solution = Solution()
print(solution.isValid("{[]}"))
