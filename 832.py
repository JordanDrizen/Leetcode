from typing import List


# class Solution:
#     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#         for i in range(len(image)):
#             image[i] = image[i][::-1]
#             image[i] = list(map(lambda x: 1 if x == 0 else 0, image[i]))
#         return image


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(image):
            image[i] = row[::-1]
            image[i] = list(map(lambda x: 1 if x == 0 else 0, image[i]))
        return image


solution = Solution()
print(solution.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
