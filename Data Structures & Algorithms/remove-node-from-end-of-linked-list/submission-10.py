# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length = length + 1
        final = length - n
        print(final)
        print(length)   
        ans = head
        lens = 0
        if lens == final:
            head = ans.next
            return head
        elif lens + 1 == final:
            if length > 2:
                head.next = ans.next.next
                return head
            else:
                ans.next = None
                return head
        while ans:
            if lens + 1 == final:
                ans.next = ans.next.next
                return head
            else:
                ans = ans.next
                lens = lens + 1
        
        