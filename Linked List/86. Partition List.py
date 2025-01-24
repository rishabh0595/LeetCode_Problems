class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        curr = head
        leftPointer = ListNode(0)
        rightPointer = ListNode(0)      
        left = leftPointer
        right = rightPointer

        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next
            curr = curr.next
        left.next = rightPointer.next
        right.next = None


        return leftPointer.next
        

"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 
Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200


"""