import math,random

def qselect(a,k):
	pivot = random.randint(0,len(a)-1)
	a[0],a[pivot]=a[pivot],a[0]
	pivot=a[0]
	left=[i for i in a if i<pivot]
	mid=[i for i in a[1:] if i>pivot]
	lleft,lmid=len(left),len(mid)
	if k<=lleft:
		return qselect(left,k)
	elif k<=lleft+1+lmid:
		return pivot,lleft
	else:
		right=[i for i in a[1:] if i>pivot]
		diff=lleft+1+lmid
		r0,r1=qselect(right,k-diff)
		return r0,r1+diff
		

def find(a,x,k):
	lst_abs=[round(math.fabs(i-x),10) for i in a]
	ele,k_small=qselect(lst_abs,k)
	print(lst_abs)
	rest=k-k_small
	res=[]
	for i,j in zip(a,lst_abs):
		if j<ele:
			res.append(i)
		elif j==ele and rest>0:
			res.append(i)
			rest-=1
	
	print(ele,k_small)
	print(res)

print(find([4,1,3,2,7,4,6], 6.2, 3))
print(find([4,1,3,2,7,4], 6.5, 3))
print(find([5,3,4,1,6,3], 3.5, 2))

