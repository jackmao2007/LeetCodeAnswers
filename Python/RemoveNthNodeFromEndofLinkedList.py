# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        front = head
        curr = None
        prev = None
        while front is not None:
            n -= 1
            if n == 0:
                curr = head
            elif curr is not None:
                prev = curr
                curr = curr.next
            front = front.next

        # case 1:
        if curr is None:
            raise ValueError
        # case 2: curr is head
        if prev is None:
            head = curr.next
            curr.next = None
            return head
        # case 3:
        else:
            prev.next = curr.next
            curr.next = None
            return head

