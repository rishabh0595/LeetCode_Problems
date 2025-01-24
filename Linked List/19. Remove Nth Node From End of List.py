class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        if not head:
            return head

        if head.next is None:
            return 
        slow = dummy
        fast = dummy

        for i in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        
        slow.next = slow.next.next

        return dummy.next


"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""