class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = 0
        rightMax = 0

        trap = 0
        left =0 
        right = len(height)-1


        while left<= right:
            if leftMax <=rightMax:
                trap += max(leftMax - height[left],0)
                leftMax = max(leftMax,height[left])
                left +=1
            else:
                trap += max(rightMax - height[right],0)
                rightMax = max(rightMax,height[right])
                right -=1
        return trap
        


            



        