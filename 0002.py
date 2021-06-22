class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_two_nodes(l1, l2):
    '''
    Leetcode 0002 (Medium): Add Two Numbers
    https://leetcode.com/problems/add-two-numbers/
    '''
    memo = 0
    dummy = ListNode(-1)
    current = dummy

    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        current.next = ListNode((val1+val2+memo) % 10)
        memo = (val1+val2+memo) // 10
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        current = current.next

    if memo > 0:
        current.next = ListNode(memo)
    
    return dummy.next
