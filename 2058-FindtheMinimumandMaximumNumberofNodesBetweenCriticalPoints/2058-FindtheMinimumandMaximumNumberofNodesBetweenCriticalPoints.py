# Last updated: 8/31/2026, 11:55:07 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
8        pos = 1
9        prev = head
10        curr = head.next
11
12        first = -1
13        last = -1
14        minDist = float('inf')
15
16        while curr and curr.next:
17            if ((curr.val > prev.val and curr.val > curr.next.val) or
18                (curr.val < prev.val and curr.val < curr.next.val)):
19
20                if first == -1:
21                    first = pos
22                else:
23                    minDist = min(minDist, pos - last)
24
25                last = pos
26
27            prev = curr
28            curr = curr.next
29            pos += 1
30
31        if first == -1 or first == last:
32            return [-1, -1]
33
34        maxDist = last - first
35
36        return [minDist, maxDist]