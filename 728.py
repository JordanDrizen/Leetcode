from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            good = False
            if '0' in str(i):
                pass
            else:
                for j in range(len(str(i))):
                    if i % int(str(i)[j]) == 0:
                        good = True
                    else:
                        good = False
                        break
            if good:
                ans.append(i)
        return ans



solution = Solution()
print(solution.selfDividingNumbers(1,22))
