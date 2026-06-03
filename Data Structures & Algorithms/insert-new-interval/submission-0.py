class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        if not intervals:
            return [newInterval]

        # Base Case 2
        if newInterval[1] < intervals[0][0]:
            res.append(newInterval)
            res.extend(intervals)
            return res

        for i in range(len(intervals)):
            newA, newB = newInterval[0], newInterval[1]
            oldA, oldB = intervals[i][0], intervals[i][1]
            
            if (oldA <= newA <= oldB) or (newA <= oldA <= newB):
                start = min(oldA, newA)
                end = max(oldB, newB)
                res = intervals[:i]

                while i + 1 < len(intervals) and end >= intervals[i+1][0]:
                    i += 1
                    end = max(end, intervals[i][1])

                res.append([start, end])
                res.extend(intervals[i+1:])
                return res
            
            if i + 1 < len(intervals) and oldB < newA < intervals[i+1][0]:
                res = intervals[:i+1]
                res.append(newInterval)
                res.extend(intervals[i+1:])
                return res
        
        intervals.append(newInterval)
        return intervals
