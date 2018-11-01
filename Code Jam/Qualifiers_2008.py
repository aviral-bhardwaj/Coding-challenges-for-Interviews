N=int(input())
f_res=[]
for iter in range(N):
	S=int(input())
	s_e=[]
	for i in range(S):
		s_e.append(input())
	Q=int(input())
	q=[]
	for i in range(Q):
		q.append(input())
	p=0
	opt_c=None
	pp=None
	while p<Q:
		i=p
		c=0
		pos=0
		while i<p+Q:
			if q[i%Q]==s_e[pos%S]:
				c+=1
				pos+=1
				continue
			pos+=1	
			i+=1
		if opt_c==None or opt_c>c:
			opt_c=c
			pp=p
		p+=1
	f_res.append((opt_c,pp))
	
print(f_res)