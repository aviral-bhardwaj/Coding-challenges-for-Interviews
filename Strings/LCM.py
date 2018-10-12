from math import gcd

def LCM(a):
	def LCM_help(a,b):
		return int((a*b)/gcd(a,b))
	
	res=a[0]
	for i in a[1:]:
		res=LCM_help(res,i)
	return res

a=[int(i) for i in input().split()]
print(LCM(a))