
from collections import defaultdict
import bisect

def isSubsequence(s,t):
    letter_indices_table = defaultdict(list)
    for index, letter in enumerate(t):
        letter_indices_table[letter].append(index)
    print(f'letter indices Table - {letter_indices_table.values()}')
    curr_match_index = -1
    for letter in s:
        if letter not in letter_indices_table:
            return False  # no match at all, early exit

        # greedy match with binary search
        indices_list = letter_indices_table[letter]
        match_index = bisect.bisect_right(indices_list, curr_match_index)

        if match_index != len(indices_list):
            curr_match_index = indices_list[match_index]
        else:
            return False  # no suitable match found, early exit
        print(f'indices list - {indices_list}')
        print(f'match index - {match_index}')
        print(f'current match index is {curr_match_index}\n')
    return True


s = "abc"
t = "abbadc"

print(isSubsequence(s,t))


