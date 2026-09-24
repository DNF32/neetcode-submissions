"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortInts = sorted(intervals, key = lambda x: x.start)

        for i in range(len(sortInts)-1):
            endI = sortInts[i].end
            startJ = sortInts[i+1].start
            if endI >startJ:
                return False

        return True

