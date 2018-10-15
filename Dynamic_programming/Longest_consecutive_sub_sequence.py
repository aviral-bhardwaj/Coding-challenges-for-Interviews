from collections import defaultdict

def lcss(l):
	hash=defaultdict(lambda:None)
	for i in l:
		hash[i]=True
	f_res=None
	max=-1
	for i in l:
		res=[]
		if hash[i] is True:
			j=i-1
			k=i+1
			res.append(i)
			while True:
				if hash[j] is None:
						break
				if hash[j] is True:
					res.append(j)
					hash[j]=False
					j-=1
			while True:
				if hash[k] is None:
						break
				if hash[k] is True:
					res.append(k)
					hash[k]=False
					k+=1
		if len(res) is not 0:
			if len(res)>max:
				max=len(res)
				f_res=res
	print(f_res)


l=[10,4,3,11,13,5,6,12,7]
lcss(l)