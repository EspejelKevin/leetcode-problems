"""

You are given two non-empty linked lists
representing two non-negative integers.
The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain
any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4] 
-> 2 + 5 = 7, 4 + 6 = 10, 3 + 4 = 7 -> 7107
-> 2 + 5 + 0 = 7, 4 + 6 + 0 = 0, 3 + 4 + 1 = 8 -> 708
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def add_two_bumbers(l1: ListNode, l2: ListNode) -> ListNode:
        carries = 0
        head = ListNode(0)
        aux = head

        while l1 or l2 or carries:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carries

            if total > 9:
                carries = total // 10
                total = total % 10
            else:
                carries = 0

            aux.next = ListNode(total)
            aux = aux.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next
