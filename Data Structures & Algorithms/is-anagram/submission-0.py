class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        m1 = self.strToMap(s)
        m2 = self.strToMap(t)
        for i, j in zip(m1,m2):
            if i !=j:
                return False
        return True


    def strToMap(self,s):
        count = 26*[0]
        for char in s:
            count[ord(char) - ord('a')]+=1
        return count