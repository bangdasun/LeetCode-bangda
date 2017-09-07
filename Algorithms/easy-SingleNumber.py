# 1. Math: from the sum
def singleNumber(array):
    return 2 * sum(set(array)) - sum(array)

singleNumber([1, 1, 2, 2, 3, 4, 3, 6, 6, -1, -2, -3, -2, -1, -3])

# 2. Hashtable: .pop() method, I didn't found .pop() in Java HashMap =.=
