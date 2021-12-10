
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = nums
        
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i] + dp[i-1]
        
        return max(dp)
        
                
