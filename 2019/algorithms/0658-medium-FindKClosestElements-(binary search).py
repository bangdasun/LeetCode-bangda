class Solution:
    def is_left_closer(self, arr: List[int], left: int, right: int, x: int) -> bool:
        if left < 0:
            return False
        if right > len(arr) - 1:
            return True
        return x - arr[left] <= arr[right] - x
    
    def get_last_position_leq_than_x(self, arr: List[int], x: int) -> int:
        n = len(arr)
        start, end = 0, n - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] < x:
                start = mid
            else:
                end = mid
        
        if arr[end] < x:
            return end
        if arr[start] < x:
            return start
        
        return start - 1 
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if arr is None or len(arr) == 0:
            return None
        
        left = self.get_last_position_leq_than_x(arr, x)
        right = left + 1
        output = []
        
        for _ in range(k):
            if self.is_left_closer(arr, left, right, x):
                output.append(arr[left])
                left -= 1
            else:
                output.append(arr[right])
                right += 1
        
        return sorted(output)
