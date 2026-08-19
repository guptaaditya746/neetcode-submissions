"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals.sort(key = lambda x: x.start)

        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                t1 = intervals[i]
                t2 = intervals[j]

                if t1.end > t2.start:
                    return False


        return True