# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def get_depth(node):
            nonlocal diameter
            
            if not node:
                return 0
            
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            # 현재 노드를 포함한 서브트리의 높이
            current_diameter = left_depth + right_depth
            
            # 현재까지의 최대 직경 업데이트
            diameter = max(diameter, current_diameter)
            
            # 현재 노드를 기준으로 한 높이 반환
            return 1 + max(left_depth, right_depth)
        
        get_depth(root)
        return diameter