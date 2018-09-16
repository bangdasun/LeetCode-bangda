"""
LeetCode 231
Easy
Power of Two

Given an integer, write a function to determine if it is a power of two

https://leetcode.com/problems/power-of-two/description/
"""

def ispower2(num):
    """
    If the number is a power of two, then it could divided by two and still a power of two.
    Can be solved using recursion
    
    Parameters
    ----------
    num: integer
    
    Return
    ------
    True / False
    """
    
    if num == 0:
        return False
    
    if num == 1:
        return True
    
    if num % 2 == 0 and num > 1:
        return ispower2(num / 2)
    else:
        return False

print("Is 2 a power of 2? ", ispower2(2))
print("Is 3 a power of 2? ", ispower2(3))
print("Is 4 a power of 2? ", ispower2(4))