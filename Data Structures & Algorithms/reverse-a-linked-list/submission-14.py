class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            storage = curr.next
            curr.next = prev
            prev = curr
            curr = storage
        return prev