class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        maxVal = 0
        size = len(heights)-1

        for i in range(len(heights)):
            while s and heights[i]< s[-1][1]:
                fSRight = heights[i]
                val = s.pop()
                if not s:
                    maxVal = max(maxVal, val[1] * (i-1-0+1))
                else:
                    fSLeftIx = s[-1][0]
                    maxVal = max(maxVal, val[1] * (i-1-fSLeftIx))
            s.append((i,heights[i]))
        
        while s:
            val = s.pop()
            if not s:
                maxVal = max(maxVal, val[1] * len(heights))
            else:
                fSLeftIx = s[-1][0]
                maxVal = max(maxVal, val[1] * (size-fSLeftIx))
        return maxVal



