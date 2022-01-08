from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = []
        for i in range(len(strs[0])):
            cols.append([row[i] for row in strs])
        ans = []
        for col in cols:
            ans.append(list(map(lambda x: ord(x), col)))
        num_deleted = 0
        for col in ans:
            if col != sorted(col):
                num_deleted += 1
        return num_deleted


solution = Solution()
print(solution.minDeletionSize(["cba", "daf", "ghi"]))
