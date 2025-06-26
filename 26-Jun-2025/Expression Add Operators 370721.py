# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int):
        answer = []
        def back( position, expression):
            #basecase
            if len(num) == position:
                if eval(expression) == target:
                    answer.append(expression) 
                return 

            for i in range(position + 1, len(num) + 1):
                temp = num[position: i]
                if len(temp) > 1 and temp[0] == "0":
                    continue
                if position == 0:
                    back( i,temp)
                else:
                    back( i,expression + "+" + temp) 
                    back( i,expression + "*" + temp) 
                    back( i,expression + "-" + temp) 
            return 
        back(0,"")
        return answer