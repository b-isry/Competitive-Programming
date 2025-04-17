# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()

        curr = head
        prev = curr
        while curr:
            if curr.val not in seen:
                seen.add(curr.val)
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next
            
            

        return head
                