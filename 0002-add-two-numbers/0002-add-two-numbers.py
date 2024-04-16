# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = None
        temp = None
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            carry = value // 10
            value = value % 10
            new_node = ListNode(value, None)
            if not head:
                head = new_node
            else:
                temp.next = new_node
            temp = new_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            temp.next = ListNode(carry, None)
        return head
            