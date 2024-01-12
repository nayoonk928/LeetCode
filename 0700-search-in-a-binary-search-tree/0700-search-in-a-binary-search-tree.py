# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 루트가 None이거나 현재 노드의 값이 찾고자 하는 값과 같다면 현재 노드 반환
        if not root or root.val == val:
            return root

        # 찾고자 하는 값이 현재 노드의 값보다 작으면 왼쪽 서브트리에서 검색
        if val < root.val:
            return self.searchBST(root.left, val)
        # 찾고자 하는 값이 현재 노드의 값보다 크면 오른쪽 서브트리에서 검색
        else:
            return self.searchBST(root.right, val)