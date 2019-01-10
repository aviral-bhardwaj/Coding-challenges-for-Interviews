class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l=len(nums1)+len(nums2)
        if l%2==1:
            return self.help_(nums1,nums2,l//2) 
        else:
            return (self.help_(nums1,nums2,l//2-1)+self.help_(nums1,nums2,l//2))/2.0
        
    def help_(self,A,B,k):
        if len(A)>len(B):
            A,B=B,A
        if not A:
            return B[k]
        if k==len(A)+len(B)-1:
            return max(A[-1],B[-1])
        i=len(A)//2
        j=k-i
        if A[i]>B[j]:
            return self.help_(A[:i],B[j:],i)
        else:
            return self.help_(A[i:],B[:j],j)