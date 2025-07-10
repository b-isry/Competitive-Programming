# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ans = ListNode()
        
        for i in lists:
            node = i
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        temp = ans
        while heap:
            temp.next = ListNode(heapq.heappop(heap))
            temp = temp.next
        return ans.next
