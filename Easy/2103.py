class Solution:
    def countPoints(self, rings: str) -> int:
        dic = {"0": '', "1": '', "2": '', "3": '', "4": '',
               "5": '', "6": '', "7": '', "8": '', "9": ''}
        for i in range(0, len(rings), 2):
            dic[rings[i+1]] += rings[i]
        ans = 0
        for val in dic.values():
            if 'R' in val and "B" in val and "G" in val:
                ans += 1
        return ans


solution = Solution()
print(solution.countPoints("G3R3R7B7R5B1G8G4B3G6"))
