class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        i=0
        d={}
        for j in range(len(s)):
            if s[j] in d:
                i=max(d[s[j]],i)
            d[s[j]]=j+1
            res=max(res,j-i+1)
        
        return res