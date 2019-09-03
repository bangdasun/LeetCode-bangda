class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words_list = text.split(' ')
        n = len(words_list)
        if n <= 2:
            return []
        
        output = []
        bigram = first + ' ' + second
        for i in range(n - 1):
            if words_list[i] + ' ' + words_list[i + 1] == bigram:
                if i + 2 <= n - 1:
                    output.append(words_list[i + 2])
        return output
