class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return None
        
        n = len(s)
        if n < 2:
            return s
        
        # matrix[i][j] == 1 -> s[i:j] is palindrome
        is_palindrome_matrix = [[False for i in range(n + 1)] for j in range(n + 1)]
        max_palindrome_length = 0
        longest_palindrome = ''
        
        for i in range(n):
            is_palindrome_matrix[i][i + 1] = True
            max_palindrome_length = 1
            longest_palindrome = s[i:i + 1]
        
        # d <= 2
        for i in range(n - 1):
            is_palindrome_matrix[i][i + 2] = s[i] == s[i + 1]
            if is_palindrome_matrix[i][i + 2]:
                max_palindrome_length = 2
                longest_palindrome = s[i:i + 2]
        
        # d > 2
        for d in range(3, n + 1):
            for i in range(n - 2):
                if i + d > n:
                    continue
                if not is_palindrome_matrix[i + 1][i + d - 1] or s[i] != s[i + d - 1]:
                    continue
                
                is_palindrome_matrix[i][i + d] = True
                max_palindrome_length = d
                longest_palindrome = s[i:i + d]
                    
        return longest_palindrome
