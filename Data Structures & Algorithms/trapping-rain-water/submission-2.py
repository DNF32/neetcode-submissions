from collections import deque

class Solution:
    def trap_sub(self, height: List[int]) -> int:
        left = 0
        right = 1

        water = 0 
        stack = deque()

        while right < len(height):
            leftVal = height[left]
            rightVal = height[right]

            if rightVal < leftVal:
                stack.append(right)
            else:
                maxWater = min(leftVal,rightVal) * (right - left -1)

                while stack:
                    i = stack.pop()
                    maxWater -= height[i]
                water +=maxWater
                left = right

            right+=1
        return water,left

    def trap(self,height: List[int])->int:
        water,left = self.trap_sub(height)

        newSlice = height[left:][::-1]
        waterTail,_ = self.trap_sub(newSlice)
        return water + waterTail

        