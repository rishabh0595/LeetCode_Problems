class Solution:
    # def majorityElement(self, nums):
    #     nums.sort()
    #     return nums[len(nums)//2]
    


    class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        elem = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == elem:
                count +=1
            else:
                count -=1
                currElem = nums[i]

                if count ==0:
                    elem = currElem
                    count +=1
        
        return elem
                


    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1 
            else:
                count -= 1

        return candidate




"""

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

"""