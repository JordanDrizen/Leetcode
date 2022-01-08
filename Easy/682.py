from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score_arr = []
        for i in range(len(ops)):
            if ops[i] == "C":
                score_arr.pop(-1)
            elif ops[i] == "D":
                score_arr.append(score_arr[-1] * 2)
            elif ops[i] == "+":
                score_arr.append(score_arr[-1] + score_arr[-2])
            else:
                score_arr.append(int(ops[i]))
        return sum(score_arr)


solution = Solution()
print(solution.calPoints(["5", "2", "C", "D", "+"]))
