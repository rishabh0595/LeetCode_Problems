def findMaxAverage(arr,k):
    n = len(arr)
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum/k    

nums=[9,7,3,5,6,2,0,8,1,9]
k=5
print(findMaxAverage(nums,k))