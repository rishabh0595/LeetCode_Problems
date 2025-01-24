class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            print(key)
            result[key].append(s)

        return list(result.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)    
        print(f'ans before  is {ans}')

        for s in strs:
            sortedString = sorted(s)
            key = tuple(sortedString) # We used tuple because for dict , 
            #list can not be used as a key because they are mutable and for hashing function key can not chnge
            print(key)
            ans[key].append(s)
        
        # print(f'ans after is {ans}')
        return list(ans.values())

"""

Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

"""

