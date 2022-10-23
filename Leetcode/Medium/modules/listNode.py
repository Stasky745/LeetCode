from typing import Optional


class ListNode:
    def __init__(self, valuesList = None, val=0, next=None):
        if not valuesList or len(valuesList) == 0:
            self.val = val
            self.next = next
        else:
            self.val = valuesList[0]
            self.next = None

            last = self

            for n in range(1, len(valuesList)):
                last.next = ListNode([], valuesList[n], None)
                last = last.next

    def print(self):
        res = []
        head = self

        while head:
            res.append(head.val)
            head = head.next
        
        print(res)