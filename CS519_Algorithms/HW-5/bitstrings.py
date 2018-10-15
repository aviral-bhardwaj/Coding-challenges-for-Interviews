import math
def num_no(n1):	
	def num_no_help(n,d={0:1,1:2}):
		if n in d:
			return d[n]
		d[n]=num_no_help(n-1)+num_no_help(n-2)
		return d[n]
		
	return num_no_help(n1)

def num_yes(n):	
	t=math.pow(2,n)
	return int(t-num_no(n))
	
print(num_no(3))
print(num_yes(3))