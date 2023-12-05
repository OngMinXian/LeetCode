# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        
        # Initialize variables
        prev_node = None
        curr_node = head

        while curr_node != None:
            
            # Save next node in a variable
            next_node = curr_node.next

            # Swaps direction
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

solution = Solution()
solution.reverseList(head)

