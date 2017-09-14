# https://leetcode.com/problems/palindrome-number/description/

def isPalindrome(x):
    x_str = str(x)

    if len(x_str) < 1:
        return True

    if len(x_str) == 2:
        if x_str[0] == x_str[1]:
            return True
        else:
            return False

    if x_str[0] == x_str[len(x_str) - 1]:
        return isPalindrome(int(x_str[1:-1]))
    else:
        return False

def isPalindrome2(x):
    return str(x) == str(x)[::-1]