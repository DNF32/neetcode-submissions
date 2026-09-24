from collections import Counter, defaultdict
class Solution:
    def has(self,window,need):
        for key, value in need.items():
            if window[key] < value:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)

        sizeBest = 1001
        bestString = ""

        left = 0
        for right, char in enumerate(s):
            if char in need:
                window[char] +=1
            
            while self.has(window,need):
                if sizeBest> right - left + 1:
                    sizeBest = right-left+1
                    bestString = s[left:right+1]

                window[s[left]] -=1
                left +=1

        return bestString
                            
                    




                






