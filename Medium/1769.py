from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        index_list = []
        index = 0
        ans = [0] * len(boxes)
        while "1" in boxes[index:]:
            index_list.append(boxes.index("1", index))
            index = boxes.index("1", index) + 1
        for i in range(len(boxes)):
            for j in index_list:
                ans[i] += abs(i - j)
        return ans


solution = Solution()
print(solution.minOperations("001011"))
