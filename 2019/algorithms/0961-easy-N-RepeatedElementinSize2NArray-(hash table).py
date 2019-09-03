class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        # M = 2N
        M = len(A)
        A_count = {}
        for num in A:
            if num not in A_count:
                A_count[num] = 1
            else:
                A_count[num] += 1
                
            if A_count[num] == M / 2:
                return num
        
        return None


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        # M = 2N
        M = len(A)
        left, right = 0, M - 1
        mid = (left + right) // 2
        A_sorted = sorted(A)
        if A_sorted[mid] == A_sorted[mid + 1]:
            return A_sorted[mid]
        else:
            if A_sorted[mid] == A_sorted[0]:
                return A_sorted[mid]
            else:
                return A_sorted[mid + 1]
        
        return None
