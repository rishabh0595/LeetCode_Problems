"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807."""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumlist1 = reverse(self, l1)
        sumlist2 = reverse(self, l2)
        finalsum = sumlist1 + sumlist2
        # print(finalsum)

        # finalsum=self.reverse(self,l1)+self.reverse(self,l2)
        return reverseAndAdd(self, finalsum)


def reverse(self, l1):
    sum1 = 0
    x = 1

    while (l1 is not None):
        sum1 = (l1.val * x) + sum1
        x = x * 10

        l1 = l1.next
    return (sum1)


def reverseAndAdd(self, finalsum):
    lns = []
    string = str(finalsum)

    for i in string:
        l = ListNode(int(i))
        if len(lns) != 0:
            l.next = lns[-1]

        lns.append(l)
    return lns[-1]
