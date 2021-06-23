# Leetcode 0141 (Easy): Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        first, second = head, head
        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second: 
                return True
        return False
