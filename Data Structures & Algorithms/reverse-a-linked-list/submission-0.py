# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        maps = []
        curr = head
        while curr:
            maps.append(curr.val)
            curr = curr.next
        maps
        new = ListNode(maps.pop())
        final = new
        while maps:
            new.next = ListNode(maps.pop())
            new = new.next
        return final
        