from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic = {"type": 0, "color": 1, "name": 2}
        ans = 0
        for i in range(len(items)):
            if items[i][dic[ruleKey]] == ruleValue:
                ans += 1
        return ans


solution = Solution()
print(
    solution.countMatches(
        [
            ["phone", "blue", "pixel"],
            ["computer", "silver", "lenovo"],
            ["phone", "gold", "iphone"],
        ],
        "color",
        "silver",
    )
)
