from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = []
        i = 0
        w = deque()
        while (i+k) <= len(nums):
            for j in range(k):
                currentVal = nums[i+j]
                currentIndex = i+j

                while w and w[-1][1] < currentVal:
                    w.pop()
                w.append((currentIndex,currentVal))
            while w[0][0]< i or w[0][0]>=i+k:
                w.popleft()
            maxList.append(w[0][1])
            i+=1
        return maxList
                        




        