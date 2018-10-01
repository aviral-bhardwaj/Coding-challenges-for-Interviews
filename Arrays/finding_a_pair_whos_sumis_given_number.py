def find_pair(l,s):
	for i in l:
		se=s-i
		l.remove(i)
		if se in l:
			return (i,se)
		l.append(i)
	return "Pair not found!"


l=[1,20,5,6,9,2,10]
s=int(input("Enter the sum : "))
print(find_pair(l,s))