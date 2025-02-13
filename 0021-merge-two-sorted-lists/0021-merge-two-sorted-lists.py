# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr =  result = ListNode()
        while list1 and list2:
            print(list1.val,list2.val)
            if list1.val<list2.val:
                curr.next = list1
                list1,curr = list1.next,list1
                print("curr",curr)
            else:
                curr.next = list2
                list2,curr = list2.next,list2
                print("curr2",curr)
        if list1 or list2:
            curr.next = list1 if list1 else list2
        return result.next
                
                
        