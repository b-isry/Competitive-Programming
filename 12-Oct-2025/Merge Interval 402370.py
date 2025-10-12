# Problem: Merge Interval - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        results = []
        
        for i in range(len(intervals)):
            if not results:
                results.append(intervals[i])
            if intervals[i][0] <= results[-1][1]:
                results[-1][1] = max(results[-1][1], intervals[i][1])
            else:
                results.append(intervals[i])
        return results
            