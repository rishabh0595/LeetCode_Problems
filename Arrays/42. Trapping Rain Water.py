class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeftArray = [0]* n
        maxRightArray = [0] * n
        result = 0

        maxLeft = 0
        maxRight = 0
        for i in range(n):
            
            if height[i] > maxLeft:
                maxLeft = height[i]
            maxLeftArray[i] = maxLeft

        for i in range(n-1,-1,-1):
            
            if height[i] > maxRight:
                maxRight = height[i]
            maxRightArray[i] = maxRight
                
        for i in range(n):
            minimum = min(maxLeftArray[i],maxRightArray[i])
            curr = minimum - height[i]
            if curr >0:
                result += curr
        
        return result



"""

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""