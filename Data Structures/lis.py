def lis(l):
	n=len(l)
	res=[1 for i in range(n)]
	back=[-1 for i in range(n)]
	for i in range(n):
		for j in list(range(i))[::-1]:
			if l[i]>l[j] and res[i]<=res[j]:
				res[i]=res[j]+1
				back[i]=j
	print(res)
	i=back[n-1]
	res_s=[]
	print(l[n-1],end=" ")
	res_s.append(l[n-1])
	while i!=-1:
		print(l[i],end=" ")
		res_s.append(l[i])
		i=back[i]
	print(res_s[::-1])
			
			
l=[10,22,9,33,21,50,41,60,80]
lis(l)