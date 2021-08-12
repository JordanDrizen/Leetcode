# class Solution:
#     def minPartitions(self, n: str) -> int:
#         nums = []
#         partitions = []
#         for num in n:
#             nums.append(int(num))
#         for i in range(max(nums)):
#             temp_s = ""
#             if all(num == 0 for num in nums):
#                 break
#             for j in range(len(nums)):
#                 if nums[j] != 0:
#                     temp_s += "1"
#                     nums[j] -= 1
#                 else:
#                     temp_s += "0"
#             partitions.append(temp_s)
#         return len(partitions)


# class Solution:
#     def minPartitions(self, n: str) -> int:
#         max_num = 0
#         for i in range(len(n)):
#             if n[i] == "9":
#                 max_num = 9
#                 break
#             max_num = max(max_num, int(n[i]))
#         return max_num


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


solution = Solution()
print(solution.minPartitions("32"))
