class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)==1 or numRows==1:
            return s
        f=0
        c=0
        n=numRows-1
        res=[]
        for i in range(numRows):
            res.append([])
    
        for i in range(len(s)):
            if i%n==0:
                if f==0:
                    f=1
                else:
                    f=0
            if f==1:
                res[c].append(s[i])
                c+=1
            elif f==0:
                res[c].append(s[i])
                c-=1
        f_res=[]
        for i in res:
            f_res.append("".join(i))
        return "".join(f_res)