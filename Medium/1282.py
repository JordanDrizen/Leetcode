from typing import List


# class Solution:
#     def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
#         ans = []
#         buckets = []
#         counter = {}
#         for size in groupSizes:
#             counter[size] = counter.get(size, 0) + 1
#         for key in counter:
#             counter[key] = int(counter[key] / key)
#         for key, val in counter.items():
#             for _ in range(val):
#                 buckets.append([key, []])
#         for i in range(len(groupSizes)):
#             size = groupSizes[i]
#             for bucket in buckets:
#                 if size == bucket[0] and len(bucket[1]) != bucket[0]:
#                     bucket[1].append(i)
#                     break
#         for bucket in buckets:
#             ans.append(bucket[1])
#         return ans


# class Solution:
#     def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
#         ans = []
#         for i in range(len(groupSizes)):
#             if i == 0:
#                 ans.append([groupSizes[i]])
#             else:
#                 for group in ans:
#                     print(len(group))

#         return ans


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        buckets = []
        sizes = list(set(groupSizes))
        for size in sizes:
            buckets.append([size, []])
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if not buckets:
                buckets.append([size, []])
            for bucket in buckets:
                if size == bucket[0]:
                    bucket[1].append(i)
                    if len(bucket[1]) == bucket[0]:
                        ans.append(bucket[1])
                        buckets.remove(bucket)
                    break
                else:
                    buckets.append([size, []])
        return ans


solution = Solution()
print(solution.groupThePeople([2, 2, 2, 2]))
