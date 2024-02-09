# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-float('inf'))  # Dummy node for the sorted part
        curr = head  # Pointer to traverse the unsorted part
        
        while curr:
            prev = dummy
            next_node = curr.next  # Save the next node to be processed
            
            # Find the correct position to insert the current node in the sorted part
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Insert the current node into the sorted part
            curr.next = prev.next
            prev.next = curr
            
            # Move to the next node in the unsorted part
            curr = next_node
        
        return dummy.next
        