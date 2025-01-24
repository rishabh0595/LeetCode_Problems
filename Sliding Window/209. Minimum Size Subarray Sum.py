

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left  = 0
        currSum = 0
        n = len(nums)
        minWindow  = float("inf")
        for right in range(len(nums)):
            
            currSum += nums[right]
            
            while currSum >= target and left <= right:
                currSum -= nums[left]
                minWindow = min(minWindow,right -left+1)
                left = left+1

        if minWindow == float("inf"):
            return 0
        
        return minWindow
            

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        minLen = len(nums)+1
        for right in range(len(nums)):
            currSum += nums[right]

            while currSum >= target:
                minLen = min(minLen,right-left+1)
                currSum -= nums[left]
                left +=1
                
        
        return 0 if minLen > len(nums) else minLen


"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


"""