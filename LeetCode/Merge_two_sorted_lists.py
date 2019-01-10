# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import merge
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll1=[]
        while l1!=None:
            ll1.append(l1.val)
            l1=l1.next
        ll2=[]
        while l2!=None:
            ll2.append(l2.val)
            l2=l2.next
        return list(merge(ll1,ll2))