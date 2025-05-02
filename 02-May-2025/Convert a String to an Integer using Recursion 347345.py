# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

def stringToIntHelper(str, index):
    if idx == len(str):
        return 0
      
    digit = int(str[idx])
    
    return digit * (10 ** (len(str) - idx - 1)) + stringToIntHelper(str, idx + 1)

def stringToInt(str):
    return stringToIntHelper(str, 0)