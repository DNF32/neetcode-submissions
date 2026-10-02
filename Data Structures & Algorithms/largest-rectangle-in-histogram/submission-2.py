class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        rectSize = 0

        for i, heigh in enumerate(heights):
            index = i
            while stack and stack[-1][1] >= heigh:
                top = stack.pop()
                index = top[0]
                val = top[1]

                # Rotine to compute square
                rectSize = max(rectSize, val *( i - index))
            stack.append((index, heigh))
        while stack:
            top = stack.pop()
            index = top[0]
            val = top[1]

            # Rotine to compute square
            rectSize = max(rectSize, val *( len(heights) - index))
        return rectSize
        
            


        