
"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""
class Solution:

    "quick select method"
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        l = 0
        r = len(nums) - 1
        k = len(nums) - k
        
        def quickselect(l,r):
            
            pivot, p = nums[r], l
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k: return quickselect(l, p-1)
            elif p < k : return quickselect(p+1, r)
            else: return nums[p]
        
        return quickselect(l, r)
