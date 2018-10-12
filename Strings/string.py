from collections import defaultdict

def check_val(str):
	d=defaultdict(lambda:0)
	for i in str:
		if d[i] is 1:
			return False
		d[i]=1
	return True

def p_list(str,k):
	res=[]
	for i in range(len(str)-k+1):
		if check_val(str[i:i+k]):
			if str[i:i+k] not in res:
				res.append(str[i:i+k])
	return res
str=input()
k=int(input())
print(p_list(str,k))
