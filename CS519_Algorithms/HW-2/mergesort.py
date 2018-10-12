def merge(a,b):
	if a==[] or b==[]:
		return a+b
	la,lb=len(a),len(b)
	c=[]
	i,j=0,0
	while i<la and j<lb:
		if a[i] < b[j]:
			c.append(a[i])
			i+=1
		else:
			c.append(b[j])
			j+=1
	if i<la:
		while i<la:
			c.append(a[i])
			i+=1
	if j<lb:
		while j<lb:
			c.append(b[j])
			j+=1
	return c

def mergesort(a):
	l=len(a)
	if l <= 1:
		return a
	return merge(mergesort(a[:l//2]),mergesort(a[l//2:]))

print(mergesort([4, 2, 5, 1, 6, 3]))