# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1
        curr_l2 = l2

        l1_arr = []
        l2_arr = []

        while curr_l1:
            l1_arr.append(str(curr_l1.val))  
            curr_l1 = curr_l1.next
        while curr_l2:
            l2_arr.append(str(curr_l2.val))  
            curr_l2 = curr_l2.next

        int_l1 = int("".join(reversed(l1_arr)))
        int_l2 = int("".join(reversed(l2_arr)))

  
        total = list(map(int, str(int_l1 + int_l2)))[::-1]

        start = ListNode(total[0])
        head = start
        for i in range(1, len(total)):
            newNode = ListNode(total[i])
            start.next = newNode
            start = newNode

        return head
