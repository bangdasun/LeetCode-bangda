# TLE solution
from collections import deque

class Solution:
    def getNextWord(self, word: str, wordList: List[str]) -> list:
		""" Neighbors of current word """
        next_words = []
        chars = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(word)):
            curr_char = word[i]
            for char in chars:
                if char == curr_char:
                    continue
                next_word = word[:i] + char + word[i+1:]
                if next_word in wordList:
                    next_words.append(next_word)
         
        return next_words
                    
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        queue = deque([beginWord])
        visited = set([beginWord])
        distance = 1
        
        while len(queue) > 0:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return distance
                next_words = self.getNextWord(word, wordList)
                for w in next_words:
                    if w in visited:
                        continue
                    queue.append(w)
                    visited.add(w)
            distance += 1
            
        return 0
 