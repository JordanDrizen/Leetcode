class Solution:
    def minimumSum(self, num: int) -> int:
        arr = [digit for digit in str(num)]
        arr.sort()
        num_1 = arr[0] + arr[-1]
        num_2 = arr[1] + arr[2]
        return int(num_1) + int(num_2)

solution = Solution()
print(solution.minimumSum(2932))
