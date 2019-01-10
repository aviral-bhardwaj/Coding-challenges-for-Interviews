n=int(input())-1
f=0
c=0
for i in range(20):
	if i%n==0:
		if f==0:
			f=1
		else:
			f=0
	if f==1:
		print(c)
		c+=1
	elif f==0:
		print(c)
		c-=1
		