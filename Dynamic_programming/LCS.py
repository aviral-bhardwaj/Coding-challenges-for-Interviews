def lcs(s1,s2):
	def solution(t):
		print(t)
	
	ls1,ls2=len(s1),len(s2)
	m=[[(0,(0,0)) for i in s2] for i in s1]
	for i in range(1,ls1):
		for j in range(1,ls2):
			if s1[i]==s2[j]:
				m[i][j]=(1+m[i-1][j-1][0],((i-1,j-1),1))
			else:
				k=max(m[i-1][j][0],m[i][j-1][0])
				if k == m[i-1][j][0] and k == m[i][j-1][0]:
					m[i][j]=(k,((i-1,j),(i,j-1),0))
				elif k==m[i-1][j]:
				
				(max(m[i-1][j][0],m[i][j-1][0]),((i-1,j),(i,j-1)))
	#for i in m:
	#	print(i)
	solution(m[ls1-1][ls2-1])

# str1=input()
# str2=input()
str1=" ABCBDAB"
str2=" BDCABA"
lcs(str1,str2)