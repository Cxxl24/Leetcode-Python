from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional [ListNode]:
        carry = 0
        sum = 0
        dummy_head = ListNode(0)
        current_node = dummy_head

        while (l1 != None or l2 != None or carry != 0):
            val1 = 0
            val2 = 0
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            carry = sum // 10
            sum = sum % 10

            new_node = ListNode(sum)
            current_node.next = new_node
            current_node = current_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next

