import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k0 = 1
        kn =  max(piles)
        minSol = kn
    
        values = range(1,kn+1)
        left = 0
        right = kn -1

        while left <=right:
            mid = (left +right) // 2
            midValue = values[mid]
            check = 0

            for val in piles:
                check += math.ceil(val/midValue)

            if check <= h:
                right = mid - 1
                if minSol > midValue:
                    minSol = midValue
            else:
                left = mid +1
                
        return minSol
