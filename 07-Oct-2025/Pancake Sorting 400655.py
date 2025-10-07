# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        for i in range(n):
            curr_max = max(arr[0:n-i])
            j = 0
            while arr[j] != curr_max:
                j += 1
            arr[:j+1] = reversed(arr[:j+1])
            ans.append(j+1)
            arr[:n-i] = reversed(arr[:n-i])
            ans.append(n-i)
        return ans
    
    
    
    


        