class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        
        CharToWord = {}
        WordToChar = {}
        for c , w in zip(pattern , s):
            if c in CharToWord and CharToWord[c] !=w:
                return False
            if w in WordToChar and WordToChar[w] !=c:
                return False

            CharToWord[c] = w
            WordToChar[w] =c
        return True