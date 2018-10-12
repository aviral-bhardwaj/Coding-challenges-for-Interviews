import random

def qselect(k,l):
	r=random.randint(0,len(l)-1)
	pivot=l[r]
	left=[i for i in l if i<pivot]
	mid=[i for i in l if i==pivot]
	right=[i for i in l if i>pivot]
	print(left,pivot,right)
	if len(left)==k-1 :
		return pivot
	elif len(left)>k-1:
		return qselect(k,left)
	else:
		if (len(left)+len(mid)) >= k :
			return pivot 
		return qselect(k-(len(left)+len(mid)),right)
	
	
print(qselect(3, [3,5,6,9,7,4,2,1,8]))