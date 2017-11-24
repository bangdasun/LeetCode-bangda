"""
LeetCode 253 
Medium
Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required. For example, Given [[0, 30],[5, 10],[15, 20]], return 2.
"""

def meeting_rooms2(intervals):
    """
    Sort the meetings by start time, and use a list to store the end time of meeting. 
    Then go through the intervals in the list one by one, and we "pull" that meeting,
    store its end time into the list.  if the end time of current meeting is earlier than 
    the start time of next meeting, means this next meeting could use the same room, then 
    we remove it. If not, we need to hold that meeting (require extra room) 

	This could be the idea of greedy algorithm: we go through all meetings, and see if 
	the meeting could be arranged within one room. If there is a meeting conflict, then we
	need open one more room 

    Improve: we can use min-heap to store the end time of meetings
    
    Parameters
    ----------
    intervals: list of interval [start_time, end_time]
    
    Return
    ------
    num_rooms: number of conference rooms needed
    """
    lst = intervals.copy()
    if not lst or len(lst) == 0:
        return 0
    
    # sort by the start time, this would take O(nlogn) time 
    lst.sort()
    
    # store the end time of meetings
    endt = [lst[0][1]]
    for it in lst[1:]:
        if it[0] >= min(endt):
            endt.remove(min(endt))
            
        endt.append(it[1])
    
    return len(endt)

# test
intervals = [[0, 13], [5, 10], [15, 20]]
meeting_rooms2(intervals)