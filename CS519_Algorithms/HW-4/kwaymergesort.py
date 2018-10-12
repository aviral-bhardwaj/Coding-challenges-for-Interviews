from heapq import merge

def kmergesort(m,k):
	length=len(m)
	if length<=1:
		return m
	split=(length-1)//k+1
	k_list=[kmergesort(m[i:i+split],k) for i in range(0,length,split)]
	return list(merge(*k_list))

print(kmergesort([4,1,5,2,6,3,7,0], 3))