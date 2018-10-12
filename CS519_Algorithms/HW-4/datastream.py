import heapq

def ksmallest(k,l):
	h=[]
	for i,el in enumerate(l):
		if i<k:
			heapq.heappush(h,el*-1)
		else:
			if el>h[0]:
				heapq.heappop(h)
				heapq.heappush(h,el*-1)
	return [i*-1 for i in h]

print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))