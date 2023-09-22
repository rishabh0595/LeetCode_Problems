def findMaxAverage(arr,k):
    sum=0
    n=len(nums)
    windowSum=0
  
  # Sum of window
    for i in range (k):
        windowSum +=nums[i]
        
    maxSum = windowSum

    # Iterate from k to n
    for i in range (k,len(nums)):
        # remove starting element and add last element
        windowSum = windowSum + nums[i] - nums[i-k]
        maxSum= max(windowSum,maxSum) # Maximum Sum
    
    # Return Average
    return (maxSum/k)
  

nums=[9,7,3,5,6,2,0,8,1,9]
k=5
print(findMaxAverage(nums,k))
