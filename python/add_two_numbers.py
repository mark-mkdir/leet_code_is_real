class Solution(object):
    def addTwoNumbers(self, l1 ,l2):

        head  = ListNode(0)
        current = head
        carryout = 0
        while l1 != None or l2 != None:
            if l1 == None:
                val1 = 0
            else:
                val1 = l1.val
            if l2 == None :
                val2 = 0
            else :
                val2 = l2.val
            total =val1 + val2 + carryout
            carryout = 0
            if total >= 10 :
                carryout = 1
                total = total - 10
            current.next = ListNode(total)
            if l1 != None:
                l1 = l1.next
            if l2 != None :
                l2 = l2.next
            current = current.next

        if carryout == 1 :
            current.next = ListNode(1)
        return head.next
    