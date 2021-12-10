
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bs_first(arr, x):
            
            res, low, high = -1, 0, len(arr)-1
            
            while low <= high:
                mid = low + (high-low) //2
                if arr[mid] == x:
                    res = mid
                    high = mid-1
                elif arr[mid] > x:
                    high = mid -1
                else:
                    low =mid+1
                    
            return res
        
        def bs_last(arr, x):
            
            res, low, high = -1, 0, len(arr)-1
            
            while low <= high:
                mid = low + (high-low)//2
                if arr[mid] == x:
                    res = mid
                    low = mid +1
                elif arr[mid] > x:
                    high = mid -1
                else:
                    low = mid +1
            return res
        
        left, right = bs_first(nums, target), bs_last(nums, target)
        
        return [left, right]
            
        
                
