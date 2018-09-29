# two pointers
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                break
        
        if i == j:
            i -= 1
            
        return i + 1, j + 1
		
# binary search
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        for i in range(n):
            diff = target - numbers[i]
            left, right = i + 1, n - 1
            while left <= right:
                m = (left + right) // 2
                if numbers[m] < diff:
                    left = m + 1
                elif numbers[m] > diff:
                    right = m - 1
                else:
                    return [i + 1, m + 1]   