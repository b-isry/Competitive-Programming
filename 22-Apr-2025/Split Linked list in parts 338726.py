# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        curr = head
        n = 0

        while curr:
            n += 1
            curr = curr.next
        
        x = n // k
        r = n % k
        arr = [None] * k

        prev = None
        temp = head

        for i in range(k):
            arr[i] = temp
            for j in range(x + (1 if r > 0 else 0)):
                prev = temp
                temp = temp.next
            
            if prev:
                prev.next = None

            if r > 0:
                r -= 1

        return arr
        

                



        