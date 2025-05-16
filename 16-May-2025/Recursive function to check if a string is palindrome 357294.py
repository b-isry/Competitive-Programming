# Problem: Recursive function to check if a string is palindrome - https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/

def isPalindromeUtil(s, left, right):

    if left >= right:
        return True
    
    if s[left] != s[right]:
        return False

    return isPalindromeUtil(s, left + 1, right - 1)


def isPalindrome(s):
    left = 0
    right = len(s) - 1
    return isPalindromeUtil(s, left, right)

if __name__ == "__main__":
    s = "abba"
    if isPalindrome(s):
        print("Yes")
    else:
        print("No")