import heapq

def nbestc(a,b):
	def put(i,j):
		if 0 <= i <n and 0<=j<n and (i,j) not in used:
			used.add((i,j))
			heapq.heappush(h,((sa[i]+sb[j],sb[j]),(sa[i],sb[j]),i,j))
	
	print(a,b)
	sa=sorted(a)
	sb=sorted(b)
	h=[]
	used=set()
	n=len(a)
	put(0,0)
	res=[]
	for _ in range(n):
		_,xy,i,j=heapq.heappop(h)
		yield xy
		put(i+1,j)
		put(i,j+1)

a, b = [4, 1, 5, 3], [2, 6, 3, 4]


print(list(nbestc(a, b)))



	# l=[]
	# heapq.heappush(l,(a[0]*b[0],0,0))
	# i,j=0,0
	# res=[]
	# print(a,b)
	# while i+1 < len(a) and j+1<len(b):
		# p,i,j=heapq.heappop(l)
		# res.append((a[i],b[j]))
		# if j+1<len(b):
			# heapq.heappush(l,(a[i]*b[j+1],i,j+1))
		# if i+1<len(a):
			# heapq.heappush(l,(a[i+1]*b[j],i+1,j))
		# print(res)
		# print(l)
	# return res