# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        head_ans = ListNode()
        curr1 = list1
        curr2 = list2

        ans = head_ans

        while True:
            # first check if both list empty
            if not curr1 and not curr2:
                break
            elif not curr1:
                ans.next = ListNode(curr2.val)
                ans = ans.next
                curr2 = curr2.next
            elif not curr2:
                ans.next = ListNode(curr1.val)
                ans = ans.next
                curr1 = curr1.next
            elif curr1.val < curr2.val:
                ans.next = ListNode(curr1.val)
                ans = ans.next
                curr1 = curr1.next
            else:
                ans.next = ListNode(curr2.val)
                ans = ans.next
                curr2 = curr2.next

        return head_ans.next
