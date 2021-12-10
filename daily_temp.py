
"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if not temperatures:
            return []
        ans = [0] * len(temperatures)
        stack = []
        
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_idx = stack.pop()[0]
                ans[prev_idx] = idx - prev_idx 
            
            stack.append((idx, temp))
        
        return ans
