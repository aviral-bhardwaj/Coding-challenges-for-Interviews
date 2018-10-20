r,c=[int(i) for i in input("Enter rows and columns: ").split()]
array2d=[[0 for i in range(c)] for j in range(r)]
array2d[3][3]=6
print(array2d)
for i in array2d:
	print(i)
	