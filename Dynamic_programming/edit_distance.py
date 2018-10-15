def edit_distance(s1,s2):
	l1,l2=len(s1),len(s2)
	ed=[[0 for i in range(l2+1)] for j in range(l1+1)]
	for i in range(l1+1):
		for j in range(l2+1):
			if i==0:
				ed[i][j]=j
			elif j==0:
				ed[i][j]=i
			elif s1[i-1]==s2[j-1]:
				ed[i][j]=ed[i-1][j-1]
			else:
				ed[i][j]=1+min(ed[i-1][j],ed[i][j-1],ed[i-1][j-1])
	for i in ed:
		print(i)
	return(ed[l1][l2])
	

s1=input("Enter string1: ")
s2=input("Enter string2: ")
print(edit_distance(s1,s2))