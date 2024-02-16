# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first, second = None, None
        prev = TreeNode(float('-inf'))

        def morris_traversal(root):
            nonlocal first, second, prev
            current = root

            while current:
                if not current.left:
                    if prev.val >= current.val:
                        if not first:
                            first = prev
                        second = current
                    prev = current
                    current = current.right
                else:
                    predecessor = current.left
                    while predecessor.right and predecessor.right != current:
                        predecessor = predecessor.right

                    if not predecessor.right:
                        predecessor.right = current
                        current = current.left
                    else:
                        predecessor.right = None
                        if prev.val >= current.val:
                            if not first:
                                first = prev
                            second = current
                        prev = current
                        current = current.right

        morris_traversal(root)
        first.val, second.val = second.val, first.val
        