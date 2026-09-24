class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        
        while 1< right - left:
            currentArea = (right - left) * min(heights[left],heights[right])
            if currentArea >maxArea:
                maxArea = currentArea
            
            # we need to see if part of the equation is not 0
            newLeft = left +1
            newRight = right -1

            if heights[left] < heights[right]:
                left = newLeft
            else:
                right = newRight
        finalArea = (right - left) * min(heights[left],heights[right])

        return max(maxArea, finalArea)
            

