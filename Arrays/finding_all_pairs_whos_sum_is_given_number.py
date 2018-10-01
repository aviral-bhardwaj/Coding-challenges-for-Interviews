def find_pair(l,s):
	k=0
	for i in l:
		se=s-i
		l.remove(i)
		if se in l:
			print((i,se))
			l.remove(se)
			k=1
		l.append(i)
	if k==0:
		return "Pair not found!"
	else:
		return "Above metioned pairs are found!"


l=[1,20,5,6,9,2,10,8,7]
s=int(input("Enter the sum : "))
print(find_pair(l,s))