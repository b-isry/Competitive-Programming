# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.events = []
        self.starts, self.ends = [], []

    def book(self, startTime: int, endTime: int) -> bool:
        left, right = 0, len(self.ends) - 1
        found = None
        while left <= right:
            mid = (left + right) // 2

            if self.ends[mid] <= startTime:
                left = mid + 1
            else:
                found = mid
                right = mid - 1
        
        if found != None and self.starts[found] < endTime:
            return False
        
        self.ends.insert(left, endTime)
        self.starts.insert(left, startTime)
        return True
                
