def Maxheapify(a,i):
	l=2*i+1
	r=2*i+2
	if l<len(a) and a[l]>a[i]:
		largest=l
	else:
		largest=i
	if r<len(a) and a[largest]<a[r]:
		largest=r
	if i is not largest:
		a[largest],a[i]=a[i],a[largest]
		Maxheapify(a,largest)
	
def HeapSort(a):
	if len(a) is 0:
		return
	print(a[0])
	a[0]=a[len(a)-1]
	a.pop()
	Maxheapify(a,0)
	HeapSort(a)
	
	
def BuildMaxHeap(a):
	for i in range(int(len(a)/2))[::-1]:
		Maxheapify(a,i)
	HeapSort(a)

a=[7,6,1,3,4,3,8,10,5,9]
BuildMaxHeap(a)

