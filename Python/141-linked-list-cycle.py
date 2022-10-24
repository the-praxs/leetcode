# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head         # slow and fast pointers
        
        while fast and fast.next:       
            slow = slow.next            # slow pointer moves one step
            fast = fast.next.next       # fast pointer moves two steps
            
            if slow == fast:            # if slow and fast pointers meet, there is a cycle
                return True
                
        return False