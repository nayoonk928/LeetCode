class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
    
        result = [intervals[0]]
    
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            prev_start, prev_end = result[-1]
    
            if curr_start <= prev_end:
                result[-1] = [prev_start, max(curr_end, prev_end)]
            else:
                result.append([curr_start, curr_end])
    
        return result