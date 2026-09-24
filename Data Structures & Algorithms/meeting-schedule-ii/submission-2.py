"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([meet.start for meet in intervals])
        ends = sorted([meet.end for meet in intervals])

        left = 0
        right = 0

        countActive = 0
        maxActive = 0

        while left <= len(intervals)-1:
            currentS=starts[left]
            firstE = ends[right]

            if currentS < firstE:
                countActive +=1
                maxActive = max(maxActive,countActive)
                left +=1
            else:
                countActive -=1
                right +=1
        return maxActive
            




        
        