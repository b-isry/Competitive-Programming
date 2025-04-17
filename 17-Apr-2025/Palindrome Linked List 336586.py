# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        curr = head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        n = len(arr)
        left, right = 0, n-1
        while left  < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True

        