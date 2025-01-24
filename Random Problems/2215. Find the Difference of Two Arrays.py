def findDifference(nums1,nums2):

    dict_1={}
    dict_2={}
    answer=[[0,0]]*2
    for i in range(len(nums1)):
        if nums1[i] in dict_1:
            dict_1[nums1[i]] +=1
        else:
            dict_1[nums1[i]]=1
    
    for i in range(len(nums2)):
        if nums2[i] in dict_2:
            dict_2[nums2[i]] +=1
        else:
            dict_2[nums2[i]]=1


    print(f'dict_1 is {dict_1.keys()}')
    print(f'dict_2 is {dict_2.keys()}')
    index_1=0
    index_2=0

    for i in range(len(nums1)):
        if nums1[i] not in dict_2:
            print(f'nums1[i] is {nums1[i]}')
            answer[0][index_1]=nums1[i]
            index_1 +=1

        if nums2[i]  not in dict_1:
            answer[1][index_2]=nums2[i]
            index_2 +=1
            print(f'nums2[i] is {nums2[i]}')
    
   
    return answer


nums1 =[1,2,3]
nums2 =[2,4,6]
print(findDifference(nums1,nums2))