class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-",   "-...", "-.-.", "-..",  ".",    "..-.", "--.",
                "....", "..",   ".---", "-.-",  ".-..", "--",   "-.",
                "---",  ".--.", "--.-", ".-.",  "...",  "-",    "..-",
                "...-", ".--",  "-..-", "-.--", "--.."]
        letter = 'abcdefghijklmnopqrstuvwxyz'
        dct = {}
        for idx, l in enumerate(letter):
            dct[l] = code[idx]
            
        transform = []
        for w in words:
            s = ''
            for i in w:
                s += dct[i]
            transform.append(s)
        
        return len(set(transform))