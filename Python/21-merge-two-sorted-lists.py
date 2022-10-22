# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()     # Merged list head
        tail = mergedList           # Merged list tail

        # While both lists are not empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1       # Add list1 node to tail list
                list1 = list1.next      # Move list1 to next node
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next            # Move tail to next node

        tail.next = list1 or list2      # Add non-empty list to tail list

        return mergedList.next          # Return next of merged list to skip 0