"""
LeetCode 252 
Easy
Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings. For example, Given [[0, 30],[5, 10],[15, 20]], return false.
"""

def meeting_rooms(intervals):
    """
    Sort the meetings by start time, then compare the last meeting's end time and next meeting's start time
    
    Parameters
    ----------
    intervals: list of interval [start_time, end_time]
    
    Return
    ------
    True / False
    """
    lst = intervals.copy()
    if not lst or len(lst) == 0:
        return False
    
    # sort by the start time, this would take O(nlogn) time 
    lst.sort()
    
    end = lst[0][1]
    for it in lst[1:]:
        # compare the start time of next meeting with the end time of current meeting
        if it[0] < end:
            return False
            
        end = max(end, it[1])
    
    return True

# test
intervals = [[0, 13], [5, 10], [15, 20]]
meeting_rooms(intervals)