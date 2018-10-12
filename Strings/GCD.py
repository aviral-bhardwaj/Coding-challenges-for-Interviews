from math import gcd
def GCD(a):
	res=a[0]
	for i in a[1:]:
		res=gcd(res,i)
	return res

a=[int(i) for i in input().split()]
print(GCD(a))
