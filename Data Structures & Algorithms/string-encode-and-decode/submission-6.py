from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        msg = []

        i = 0
        while i < len(s):   
            j =i 
            while s[j] != "#":
                j+=1
        
            size = int(s[i:j])

            j+=1
            msg.append(s[j:j+size])
            i = j + size
        return msg
