# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        ptr1 = head
        ptr2 = prev
        max_twin = float('-inf')

        while ptr2:
            twin_sum = int(ptr1.val) + int(ptr2.val)
            max_twin = max(twin_sum, max_twin)
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return max_twin

        
        


