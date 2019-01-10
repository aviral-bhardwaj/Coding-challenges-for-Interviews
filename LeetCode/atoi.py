class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str.strip())==0:
            return 0
        a=['0','1','2','3','4','5','6','7','8','9','.','-','+']
        s=str.split()[0].strip()
        if len(s)==0 or (len(s)==1 and (s[0]=='+' or s[0]=='-')):
            return 0
        if s.count('.')>1:
            return 0
        ss=""
        for i in s:
            if i=='-' and s.index('-')!=0 or s.count('-')>1:
                return 0
            if i=='+' and s.index('+')!=0 or s.count('+')>1:
                return 0
            if i not in a:
                break
            else:
                ss+=i
        if len(ss)==0:
            return 0
        s=ss
        if s[0]=='-':
            print(s)
            r=int(s)
            if r<-1*pow(2,31):
                return -1*pow(2,31)
            else:
                return r
        elif s[0]=='+':
            r=int(s)
            if r>pow(2,31):
                return pow(2,31)-1
            else:
                return r
        else:
            r=int(float(s))
            if r>pow(2,31):
                return pow(2,31)-1
            else:
                return r
				
o=Solution()
print(o.myAtoi("  -0012a42"))