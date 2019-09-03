class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters is None:
            return None
        
        n = len(letters)
        if n == 0:
            return None
        
        start, end = 0, n - 1
        if letters[-1] <= target:
            return letters[0]
        
        while start + 1 < end:
            mid = (start + end) // 2
            if letters[mid] < target:
                start = mid
            elif letters[mid] == target:
                start = mid
            else:
                end = mid
        
        if letters[start] > target:
            return letters[start]
        if letters[end] > target:
            return letters[end]
