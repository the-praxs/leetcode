class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:    # If the new interval is to the left of the current interval
                newIntervals.append(newInterval)    # Add the new interval to the new intervals
                return newIntervals+intervals[i:]   # Add the rest of the intervals to the new intervals and return
            elif newInterval[0] > intervals[i][1]:  # If the new interval is to the right of the current interval
                newIntervals.append(intervals[i])   # Add the current interval to the new intervals
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]  # Merge the new interval with the current interval
                
        newIntervals.append(newInterval)            # Add the new interval to the new intervals
                
        return newIntervals