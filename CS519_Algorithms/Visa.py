def A(t_hours,no_days,max_h_day):
	a=[[0 for i in range(no_days+1)] for j in range(t_hours+1)]
	for i in range(t_hours+1):
		for j in range(no_days+1):
			if i==0:
				continue
			else:
				if (j/i) < max_h_day:
					a[i][j]=1
	for i in a:
		print(i)
	
	
	

total_hours=int(input())
max_day=int(input())
pattern=input()
res=total_hours
c=0
for i in pattern:
	print(i)
	if i is not '?':
		c+=1
		res-=int(i)
#A(res,7-c,max_day)
A(4,4,2)