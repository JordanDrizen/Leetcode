
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            if low <= root.val <= high:
                self.sum += root.val
            if root.val < low:
                self.rangeSumBST(root.right, low, high)
            elif root.val > high:
                self.rangeSumBST(root.left, low, high)
            else:
                self.rangeSumBST(root.right, low, high)
                self.rangeSumBST(root.left, low, high) 
        return self.sum



solution = Solution()
print(solution.rangeSumBST([10,5,15,3,7,None,18], 7, 15))
