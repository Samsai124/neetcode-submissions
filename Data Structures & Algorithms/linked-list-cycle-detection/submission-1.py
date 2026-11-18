# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        point1 = head
        point2 = head.next
        while point1 and point2:
            if point1 == point2:
                return True
            point1 = point1.next
            if point2.next:
                point2 = point2.next.next
            else:
                return False
        return False
        