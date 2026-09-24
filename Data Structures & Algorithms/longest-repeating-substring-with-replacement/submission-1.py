class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = 26*[0]
        currentMax = 0
        maxLen = 0

        left = 0
        for i in range(len(s)):
            index =ord(s[i])-ord('A')
            counter[index] +=1

            currentMax = max(currentMax,counter[index])
            
            currentWindow = i- left +1
            if (currentWindow - currentMax) <= k:
                maxLen = max(maxLen, currentWindow)
                continue
            while (i -left +1 - currentMax) >k:
                index =ord(s[left])-ord('A')
                counter[index] -=1

                left+=1 
                currentMax = max(counter)
        return maxLen


