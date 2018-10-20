r,c=[int(i) for i in input("Enter rows and columns: ").split()]
max=-1
pos=-1
array2d=[]
for i in range(r):
	row=[int(i) for i in input().split()]
	array2d.append(row)
	c=0
	for j in row:
		if j==1:
			c+=1
	if c>max:
		max=c
		pos=i
for i in array2d:
	print(i)
print("Mas number of 1's present in row : ",pos)