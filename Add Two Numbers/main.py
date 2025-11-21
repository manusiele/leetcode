class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)        # start of result list
        current = dummy            # pointer to build the list
        carry = 0                  # carry from addition

        while l1 or l2 or carry:   # run while digits or carry exist
            # get digit values
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0

            # add values
            total = val1 + val2 + carry
            carry = total // 10    # update carry
            digit = total % 10     # digit to store

            # append new digit node
            current.next = ListNode(digit)
            current = current.next

            # move forward in lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next          # return head of result
