# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        total_tank = 0
        i = 0

        for j in range(n):
            total_tank += gas[j] - cost[j]
            tank += gas[j] - cost[j]

            if tank < 0:
                i = j + 1
                tank = 0

        return i if total_tank >= 0 else -1