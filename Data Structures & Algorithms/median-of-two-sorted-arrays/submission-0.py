import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        n, m = len(nums1),len(nums2)
        if n>m:
            A,B = B,A
            n, m = m,n  

        total = n + m
        half = (total + 1) // 2
    
        left, right = 0,n
        
        while left <= right:
            i = (left + right) // 2
            j = half - i
    
            Aleft  = float("-inf") if i == 0 else A[i - 1]
            Aright = float("inf")  if i == n else A[i]
    
            Bleft  = float("-inf") if j == 0 else B[j - 1]
            Bright = float("inf")  if j == m else B[j]
    
            if Aleft > Bright:
                right = i - 1
            elif Bleft > Aright:
                left = i + 1
            else:
                if total % 2 == 1:
                    return max(Aleft, Bleft)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2