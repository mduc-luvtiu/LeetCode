# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        i = 0
        remind = 0
        while (l1 is not None) or (l2 is not None) or (remind != 0):
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0
            sum = a+b+remind
            digit = sum%10
            remind = sum//10

