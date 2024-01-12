# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            
            if not node or node.val == val:
                return node
    
            if val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        
        return dfs(root)