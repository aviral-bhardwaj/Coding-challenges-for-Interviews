r,c=[int(i) for i in input("Enter rows and columns: ").split()]
array2d=[]
for i in range(r):
	row=[int(i) for i in input().split()]
	array2d.append(row)
for i in range(1,r):
	for j in range(1,c):
		if array2d[i][j]!=0:
			array2d[i][j]=1+min(array2d[i-1][j-1],array2d[i-1][j],array2d[j][i-1])
for i in array2d:
	print(i)