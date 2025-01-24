class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i = 0

        currVal = nums[i]
        n = len(nums)
        k = k % n

        count = 0
        index = 0
        nextVal = currVal+1
        
        while count < n:
            
            nextVal = nums[(index +k) % n]  
            

            nums[(index +k) % n] = currVal
            currVal = nextVal
            index = (index +k) % n
            count +=1

            # Check for cycle detection
            if (index)== i:
                index = i+1
                i +=1
                if i >=n:
                    break
                currVal = nums[index]

            # print(nums)



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1
"""

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
"""