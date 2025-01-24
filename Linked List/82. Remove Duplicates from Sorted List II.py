class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.next and current.next.val == current.next.next.val:
                # Duplicate found -> iterate until we reach a distinct value
                val = current.next.val
                while current.next and current.next.val == val:
                    current.next = current.next.next
            else:
                current = current.next

        return dummy.next


"""

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
 
"""