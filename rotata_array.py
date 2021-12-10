
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        
        [1,2,3,4,5,6,7]
        [7654321]
        [5674321]
        """
        
        
        def swap(start, end):   
            while start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
      
        k = k% len(nums)
        swap(0, len(nums)-1)
        swap(0, k-1)
        swap(k, len(nums)-1)
                
