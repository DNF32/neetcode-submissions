from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        func = lambda w: "".join(["\\", str(len(w)),"-", w])
        return "".join(map(func, strs))

    def decode(self, s: str) -> List[str]:
        msg = []
        i = 0
        while i < len(s):
            if s[i] == "\\" and i + 1 < len(s) and s[i + 1].isdigit():
                i += 1
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                num = int(s[start:i])
                i+=1
                word = s[i:i + num]
                i += num
                msg.append(word)
            else:
                i += 1  
        return msg
