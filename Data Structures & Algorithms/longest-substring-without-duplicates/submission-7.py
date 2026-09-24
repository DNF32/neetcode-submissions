class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        maxLenght = 0

        left = 0
        right = 0
        while right <len(s):
            if s[right] in counter:
                currentLenght = right - 1 - left +1
                if currentLenght > maxLenght:
                    maxLenght = currentLenght

                left = max(left, counter[s[right]] + 1)
                counter[s[right]] = right

                right =  right + 1
            else:
                currentLenght = right - left +1
                if currentLenght > maxLenght:
                    maxLenght = currentLenght

                counter[s[right]] = right
                right =right + 1 
        return maxLenght

        