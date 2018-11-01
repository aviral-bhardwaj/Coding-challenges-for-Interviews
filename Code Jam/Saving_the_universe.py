import heapq 
from collections import defaultdict
N=int(input())
f_res=[]
for iter in range(N):
	d=defaultdict(lambda:0)
	h=[]
	S=int(input())
	s_e=[]
	for i in range(S):
		s_e.append(input())
	Q=int(input())
	q=[]
	for i in range(Q):
		q.append(input())
	for i in q:
		d[i]+=1
	for i in s_e:
		if i not in d:
			h.append((0,i))
	[h.append((d[i],i)) for i in d]
			
	heapq.heapify(h)
	print(h)
		
	