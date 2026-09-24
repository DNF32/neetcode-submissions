from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = []
        w = deque()
        for i in range(k):
            while w and w[-1][1] < nums[i]:
                w.pop()
            w.append((i, nums[i]))
        
        maxList.append(w[0][1])
        i = 1
        while (i+k) <= len(nums):
            currentVal = nums[i+k-1]
            currentIndex = i+k-1
            while w and w[-1][1] < currentVal:
                w.pop()
            w.append((currentIndex,currentVal))

            while w[0][0]< i or w[0][0]>=i+k:
                w.popleft()
            maxList.append(w[0][1])
            i+=1
        return maxList
                        




        