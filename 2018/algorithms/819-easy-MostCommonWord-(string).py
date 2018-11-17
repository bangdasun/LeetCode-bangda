class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        paragraph_processed = ''
        for s in paragraph:
            if s.isupper():
                s = s.lower()
                
            if s not in letters:
                paragraph_processed += ' '
            else:
                paragraph_processed += s
                
        dct = {}
        max_count = 0
        output = ''
        for s in paragraph_processed.split():
            if s not in banned:
                dct[s] = dct.get(s, 0) + 1
                if dct[s] > max_count:
                    max_count = dct[s]
                    output = s
        
        return output