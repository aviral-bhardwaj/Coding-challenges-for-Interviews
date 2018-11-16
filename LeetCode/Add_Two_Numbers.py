# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_ele=[]
        while l1!=None:
            l1_ele.append(l1.val)
            l1=l1.next
        l2_ele=[]
        while l2!=None:
            l2_ele.append(l2.val)
            l2=l2.next
        print(l1_ele,l2_ele)
        
        return [int(i) for i in str(int("".join(str(i) for i in l1_ele[::-1])) + int("".join(str(i) for i in l2_ele[::-1])))][::-1]