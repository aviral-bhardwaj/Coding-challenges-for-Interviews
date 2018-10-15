def msis(l):
	n=len(l)
	a=[(0,-1) for i in range(n)]
	a[0]=(l[0],0)
	max=-1
	f=None
	back=None
	for i in range(1,n):
		j=i-1
		a[i]=(l[i],i)
		while j>=0:
			if l[i]>l[j] and a[j][0]+l[i] > a[i][0]:
				a[i]=(a[j][0]+l[i],j)
				if a[i][0] >max:
					max=a[i][0]
					f=a[i]
					back=i
			j-=1
			
	res=[]
	res.append(l[back])
	while True:
		res.append(l[a[back][1]])
		back=a[back][1]
		if a[back][1] is back:
			break
	print(res[::-1])
	
	
	# print(a)
	# print(f)
	# print(back)

l=[20,3,1,15,16,2,12,13]
msis(l)