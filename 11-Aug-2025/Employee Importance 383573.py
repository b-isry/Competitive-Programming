# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        subordinates = defaultdict() 
        ids = defaultdict() 
        for employee in employees:
            subordinates[employee.id] = employee.subordinates
            ids[employee.id] = employee.importance
        res = 0
        queue = deque()
        queue.append(subordinates[id])
        res += ids[id]
        while queue:
            sub = queue.popleft()
            for i in sub:
                queue.append(subordinates[i])
                res += ids[i]
        return res

