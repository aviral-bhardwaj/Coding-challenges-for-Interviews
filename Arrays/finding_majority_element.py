def find_majority(l):
	i=int(len(l)/2)-1
	for j in range(len(l)-i):
		if l[j]==l[j+i]:
			return ("Majority element found ",l[j])
	return ("Majority element not found ")


l=[1,1,1,1,2,3,4]
print(find_majority(l))