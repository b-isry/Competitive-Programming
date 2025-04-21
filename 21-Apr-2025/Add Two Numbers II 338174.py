# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        temp1 = l1
        temp2 = l2

        while temp1:
            num1.append(temp1.val)
            temp1 = temp1.next
        
        while temp2:
            num2.append(temp2.val)
            temp2 = temp2.next

        n1 = int(''.join(map(str, num1)))
        n2 = int(''.join(map(str, num2)))

        total = n1 + n2
        total = [int(i) for i in str(total)]


        head = ListNode(total[0])
        curr = head
        for num in total[1:]:
            curr.next = ListNode(num)
            curr = curr.next
        return head

