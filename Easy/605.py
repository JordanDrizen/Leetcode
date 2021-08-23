from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if 0 in flowerbed:
                return True
            elif 1 in flowerbed and n == 1:
                return False
            else:
                return True
        for i in range(len(flowerbed)):
            if n == 0:
                break
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif (
                i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0
            ):
                flowerbed[i] = 1
                n -= 1
            else:
                if (
                    flowerbed[i] == 0
                    and flowerbed[i - 1] == 0
                    and flowerbed[i + 1] == 0
                ):
                    flowerbed[i] = 1
                    n -= 1
        return n == 0


solution = Solution()
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))
