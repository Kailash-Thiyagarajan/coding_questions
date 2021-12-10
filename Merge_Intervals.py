
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        
        result = []
        
        for i in range(len(intervals)):
            if not result or intervals[i][0] > result[-1][1] :
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result
        
                
