# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = ""
        while head.next:
            ans += str(head.val)
            head = head.next
        ans += str(head.val)
        ans = int(ans, 2)
        return ans


solution = Solution()
print(solution.buildArray([3, 0, 1, 2]))
