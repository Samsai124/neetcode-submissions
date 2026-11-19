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
            length += 1
        final = length - n
        print(length)
        print(final)
        leng = 0
        last = head
        if (leng) == final:
            head = head.next
        if leng == final:
            head.next = None
        while last:
            last = last.next
            leng += 1
            if (leng+1) == final:
                last.next = last.next.next
        
        return head
