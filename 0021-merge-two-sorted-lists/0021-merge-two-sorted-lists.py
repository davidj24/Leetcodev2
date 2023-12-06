# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            if not list2:
                return None
            else:
                return list2
        if not list2:
            return list1

        #merging the lists
        current = list1
        while current.next:
            current = current.next
        current.next = list2

        # now to sort
        replacer = 0
        sort = False
        while not sort:
            current = list1
            sort = True
            while current.next:
                print(current.val, current.next.val)
                if current.val > current.next.val:
                    replacer = current.val
                    current.val = current.next.val
                    current.next.val = replacer
                    replacer = 0
                    sort = False
                current = current.next
        return list1


# optimized solution by someone else
#        dummy = cur = ListNode(0)
#        while l1 and l2:
#            if l1.val < l2.val:
#                cur.next = l1
#                l1 = l1.next
#            else:
#                cur.next = l2
#                l2 = l2.next
#            cur = cur.next
#        cur.next = l1 or l2
#        return dummy.next



        