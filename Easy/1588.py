from typing import List

# class Solution:
#     def sumOddLengthSubarrays(self, arr: List[int]) -> int:
# length = [i for i in range(1, len(arr) + 1)]
# length = list(filter(lambda x: x % 2 == 1, length))
# for val in length:
#     for i in range(val):
#         print(arr[i], i)
# return


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(1, len(arr) + 1):
            for j in range(len(arr) - i + 1):
                if len(arr[j : i + j]) % 2 == 1:
                    ans += sum(arr[j : i + j])
        return ans


solution = Solution()
print(solution.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
