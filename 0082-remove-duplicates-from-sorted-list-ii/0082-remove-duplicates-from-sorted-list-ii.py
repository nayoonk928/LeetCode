# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        while prev.next and prev.next.next:
            curr = prev.next
            # Check if the current node has duplicates
            if curr.val == curr.next.val:
                # Move curr to the last duplicate node
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Skip all duplicates
                prev.next = curr.next
            else:
                # Move to the next node
                prev = prev.next
        
        return dummy.next
            