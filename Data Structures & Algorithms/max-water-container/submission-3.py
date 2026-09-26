class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggestArea= 0
        left = 0
        right = len(heights)-1

        while left< right:
            currentArea = right - left 
            biggestArea = max(biggestArea, currentArea * min(heights[left],heights[right]))

            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return biggestArea

        