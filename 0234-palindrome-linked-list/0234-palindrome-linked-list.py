# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []

        if not head:
            return True
    
        node = head
        while node:
            arr.append(node.val)
            node = node.next
    
        while len(arr) > 1:
            if arr.pop(0) != arr.pop():
                return False
    
        return True
        