# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        number = 0

        temp = head
        while temp is not None:
            number += 1
            temp = temp.next
        
        if number == 1:
            return None
            
        number = number // 2

        temp = head
        for i in range(number-1):
            temp = temp.next

        temp.next = temp.next.next

        return head
        