class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []

        trap = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
    
                if not stack:
                    break
    
                leftWall = stack[-1]
                rightWall = i

                trap += (min(height[leftWall], height[rightWall]) - height[bottom]) * (rightWall - leftWall -1)

            stack.append(i)
        return trap


            



        