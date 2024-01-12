# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
    
        current_value = 0
        if low <= root.val <= high:
            current_value = root.val
    
        left_sum = self.rangeSumBST(root.left, low, high)
    
        right_sum = self.rangeSumBST(root.right, low, high)
    
        return current_value + left_sum + right_sum
        