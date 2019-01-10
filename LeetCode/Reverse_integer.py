class Solution(object):
    def reverse(self, x):
        s=str(x)
        if s[0]=='-':
            s=s[1:]
            r=int('-'+(s[::-1]))
            if r<-1*pow(2,31):
                return 0
            else:
                return int(r)
        elif s[0]=='+':
            s=s[1:]
            r=int('+'+s[::-1])
            if r>pow(2,31):
                return 0
            else:
                return int(r)
        else:
            r=int(s[::-1])
            if r>pow(2,31):
                return 0
            else:
                return int(r)