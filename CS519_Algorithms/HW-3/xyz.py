def find(lst):
	lst.sort()
	res=[]
	for z in lst:
		i=0 
		j=len(lst)-2
		lst2=[i for i in lst]
		lst2.remove(z)
		while i<j and i<len(lst2) and j>=0:
			if lst2[i]+lst2[j]==z:
				res.append((lst2[i],lst2[j],z))
				i+=1
				j-=1
			elif lst2[i]+lst2[j]>z:
				j-=1
			else:
				i+=1
	return res			

print(find([1, 4, 2, 3, 5]))