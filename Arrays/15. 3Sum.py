class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums) - 1
        result = []
        prev = float("inf")

        for k in range(len(nums)-2):
            if nums[k] == prev:
                continue
            prev = nums[k]
            target = 0 - nums[k]
            i = k+1
            j = n

            while i < j:
                if (i + 1) < j and nums[i + 1] == nums[i]:
                    if nums[i] + nums[j] + nums[k] == 0: 
                        i += 1
                        continue
                   
                currSum = nums[i]+nums[j]
                if currSum ==target:
                    result.append([nums[k],nums[i],nums[j]])
                    i+=1
                    j -= 1
                elif currSum > target:
                    j -= 1
                else:
                    i += 1
            
        return result

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for k in range(n - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue  # Skip duplicate values for `k`

            target = 0 - nums[k]
            i, j = k + 1, n - 1

            while i < j:
                currSum = nums[i] + nums[j]
                if currSum == target:
                    result.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1

                    # Skip duplicate values for `i` and `j`
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif currSum > target:
                    j -= 1
                else:
                    i += 1

        return result



"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""