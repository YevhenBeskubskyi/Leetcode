class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    '''
    Leetcode 0141 (Easy): Linked List Cycle
    https://leetcode.com/problems/linked-list-cycle/
    '''
    fast = head
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    
    return False
