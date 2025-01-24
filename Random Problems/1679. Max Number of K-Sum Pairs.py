def maxOperations(nums,k):
    dict={}
    memo=[0]*len(nums)
    count=0
    for i in range (len(nums)):
        differance = k-nums[i]
       # print(f'index is {dict[nums[i]]}')
        if differance in dict:
            if nums[i] in dict and memo[dict[nums[i]]] == 0:
                print(f'index is {dict[nums[i]]}')
                memo[i]=1
                memo[dict[nums[i]]]=1
                count=count+1
        else:
            dict[nums[i]]=i
    print(dict.keys())
    print(memo)
    return count

#nums=[3,1,3,4,3]
#k=6
nums =[1,2,3,4]
k = 5


print(maxOperations(nums,k))