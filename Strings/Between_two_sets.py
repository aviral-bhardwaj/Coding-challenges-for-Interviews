from math import gcd

def LCM(a):
	def LCM_help(a,b):
		return int((a*b)/gcd(a,b))
	
	res=a[0]
	for i in a[1:]:
		res=LCM_help(res,i)
	return res
	
def GCD(a):
	res=a[0]
	for i in a[1:]:
		res=gcd(res,i)
	return res

def between_two_sets(a,b):
	v1=LCM(a)
	v2=GCD(b)
	i=1
	c=0
	while True:
		if v2%(v1*i) is 0:
			c+=1
		i+=1
		if (v1*i) > v2:
			break
	return c
	
n,m=[int(i)for i in input().split()]
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
print(between_two_sets(a,b))