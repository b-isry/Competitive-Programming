# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = ListNode(0)
        sec = ListNode(0)

        curr = head
        f = first
        s = sec
        
        while curr:
            if curr.val < x:
                f.next = curr
                f = f.next
            elif curr.val >= x:
                s.next = curr
                s = s.next
            curr = curr.next
        
        s.next = None
        f.next = sec.next

        return first.next



