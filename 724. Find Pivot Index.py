class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        totalSum=0
        leftSum=0

        # Find total sum of array
        for num in nums:
            totalSum += num
        
        # Base Case
        if n==1 or (n==2 and nums[1]==0):
            return 0
        
        # Iterate and check if totalSum-nums[i])/2 == leftSum
        for i in range(n):
            if (totalSum-nums[i])/2 == leftSum:
                return i
            leftSum += nums[i] # Update leftSum
        
        # return -1 if no index is found
        return -1




        
