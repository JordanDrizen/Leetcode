from typing import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(goal)
        if c1.keys() != c2.keys():
            return False
        elif s == goal:
            if any([True for i, j in c1.items() if j > 1]):
                return True
        else:
            for key in c1.keys():
                if c1[key] != c2[key]:
                    return False
            indices = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    indices.append(i)
                if len(indices) == 2:
                    break
            ans = ""
            ans += s[:indices[0]]
            ans += s[indices[1]]
            ans += s[indices[0]+1:indices[1]]
            ans += s[indices[0]]
            ans += s[indices[1]+1:]
            return ans == goal



solution = Solution()
print(solution.buddyStrings("acccccb", "bccccca"))
