# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):

        # Handles edge cases
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        head = ListNode(-1)

        curr_node = head
        while list1 != None and list2 != None:
            print(curr_node.val)
            if list1.val <= list2.val:
                curr_node.next = list1
                curr_node = curr_node.next
                list1 = list1.next

            else:
                curr_node.next = list2
                curr_node = curr_node.next
                list2 = list2.next
        
        # Adds remainder
        if list1 != None:
            curr_node.next = list1
        else:
            curr_node.next = list2

        return head.next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

Solution().mergeTwoLists(list1, list2)