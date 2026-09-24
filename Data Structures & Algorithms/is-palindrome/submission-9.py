class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        for i in range(len(filtered)):
            if filtered[i]!=filtered[len(filtered)-i-1]:
                return False 
        return True 
        