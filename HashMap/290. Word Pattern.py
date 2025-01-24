
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_p_s = {}
        dict_s_p = {}
        s=s.split(" ")
        if len(s) != len(pattern):
            return False
        for c1, c2 in zip(pattern, s):
            if c1 not in dict_p_s and c2 not in dict_s_p:
                dict_p_s[c1] = c2
                dict_s_p[c2] = c1
            elif dict_p_s.get(c1) != c2 or dict_s_p.get(c2) != c1:
                return False

        return True

"""

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""