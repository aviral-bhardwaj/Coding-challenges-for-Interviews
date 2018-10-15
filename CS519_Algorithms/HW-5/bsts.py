def fact(n):
	if n==0:
		return 1
	return n*fact(n-1)

def bsts(n):
	return int(fact(2*n)/(fact(n+1)*fact(n)))

print(bsts(2))
print(bsts(3))
print(bsts(5))