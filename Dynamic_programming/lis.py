def lis(l):
	def solution(m_i):
		if m_i <=0:
			return [l[m_i]]
		return solution(back[m_i])+[l[m_i]]
	
	n=len(l)
	c=[1 for i in l]
	back=[-1 for i in l]
	m,m_i=-1,-1
	for i in range(1,n):
		j=i-1
		while j>=0:
			if l[i]>l[j] and c[j]+1>c[i]:
				c[i]=c[j]+1
				back[i]=j
				if m<c[i]:
					m=c[i]
					m_i=i
			j-=1
	#print(c,back,m,m_i)
	print(solution(m_i))
		

l=[2,3,1,5,12,10,11]
lis(l)