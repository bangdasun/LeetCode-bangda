class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        left, right = 0, n - 1
        output = []
        
        while left <= right:
            left_sq = A[left] ** 2
            right_sq = A[right] ** 2
            if left_sq < right_sq:
                output.append(right_sq)
                right -= 1
            elif left_sq > right_sq:
                output.append(left_sq)
                left += 1
            else:
                output.append(left_sq)
                if left != right:
                    output.append(right_sq)
                left += 1
                right -= 1
        
        return output[::-1]
