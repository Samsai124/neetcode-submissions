# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        l1 = list1
        l2 = list2
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val < l2.val:
            merged = ListNode(l1.val)
            final = merged
            l1 = l1.next
        else:
            merged = ListNode(l2.val)
            final = merged
            l2 = l2.next
        while l1 and l2:
            if l1.val <= l2.val:
                merged.next = ListNode(l1.val)
                merged = merged.next
                l1 = l1.next
            else:
                merged.next = ListNode(l2.val)
                merged = merged.next
                l2 = l2.next
        if l1:
            while l1:
                merged.next = ListNode(l1.val)
                merged = merged.next
                l1 = l1.next
        if l2:
            while l2:
                merged.next = ListNode(l2.val)
                merged = merged.next
                l2 = l2.next
        return final
