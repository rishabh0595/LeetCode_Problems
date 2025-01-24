


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) -1

        while i <= j:
            while i<= j and nums[i] != val:
                i +=1
            
            while i <= j and nums[j] ==val:
                j -=1
            
            if i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j -=1

        return i
            

"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
"""