class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = {}
        tLetters = {}

        if len(s) != len(t):
            return False

        for (letterS, letterT) in zip(s,t):
            sLetters[letterS]=sLetters.get(letterS,0) +1
            tLetters[letterT]=tLetters.get(letterT,0) +1
        
        return sLetters == tLetters
        