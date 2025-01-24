class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_T = {}

        hashMap_S = {}


        for elem in t:
            count_T[elem] = 1 + count_T.get(elem,0)

        left = 0 

        have = 0
        required = len(count_T)
        result = float("inf")
        min_left = -1
        min_Right = -1

        for right in range(len(s)):

            hashMap_S[s[right]] = 1 + hashMap_S.get(s[right],0)
            
            if s[right] in count_T and hashMap_S[s[right]] == count_T[s[right]]:
                have +=1
            

            while have == required:
                if right - left +1 < result:
                        min_left = left
                        min_right = right
                        result = right - left +1
                print(f'left is {left} is {s[left]} and right is {right} is {s[right]}')
                hashMap_S[s[left]] -=1
                
                if s[left] in count_T and (hashMap_S[s[left]] < count_T[s[left]]):
                # if s[left] in count_T and not (hashMap_S[s[left]] >= count_T[s[left]]):
                    have -=1
                    
                
                left +=1
        print(result)
        return s[min_left:min_right+1] if result != float("inf") else ""




"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?

"""