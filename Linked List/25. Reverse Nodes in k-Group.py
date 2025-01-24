class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0,head)

        groupPrev = dummy

        while True:
            kth = self.getKthNode(groupPrev,k)
            if kth is None:
                break
            
            groupNext = kth.next
            
            prev = kth.next
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
            
        return dummy.next

    def getKthNode(self,curr,k):
        while curr is not None and k >0:
            curr = curr.next
            k -=1
        return curr



"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

"""