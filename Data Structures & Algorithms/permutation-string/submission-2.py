from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size1 = len(s1)
        size2 = len(s2)
        if size1 > size2:
            return False
        
        pr = Counter(s1)
        runningCounter = Counter(s2[0:size1])
        if pr == runningCounter:
            return True
        i = 1
        while i + size1 <=size2:
            runningCounter[s2[i-1]]-=1
            if runningCounter[s2[i-1]]==0:
                del runningCounter[s2[i-1]]

            if s2[i+size1-1] in runningCounter:
                runningCounter[s2[i+size1-1]] +=1
            else:
                runningCounter[s2[i+size1-1]] =1

            
            if pr == runningCounter:
                return True
            i+=1
        return False

