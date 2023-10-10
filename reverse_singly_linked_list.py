# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_node = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = next_node
            next_node = curr
            curr = temp

        return next_node
