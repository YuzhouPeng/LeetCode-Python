class Solution(object):

    def swapPairs(self, head):
        if not head or not head.next:
            return head
        newstart = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(newstart)
        return head