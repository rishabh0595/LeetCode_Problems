class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        dummy = ListNode(0,head)
        right = dummy
        left = dummy 
        curr = head
        
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        
        k = k%n
        for i in range(k):
            right = right.next
        
        while right.next:
            left = left.next
            right = right.next
        
        right.next = dummy.next
        head = left.next
        left.next = None

        return head
        