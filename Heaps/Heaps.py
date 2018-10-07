from collections import deque

def max_heapify(a,i):
	l=2*i+1
	r=2*i+2
	if l<len(a) and a[l]>a[i]:
		largest=l
	else:
		largest=i
	if r<len(a) and a[r]>a[largest]:
		largest=r
	if i is not largest:
		a[i],a[largest]=a[largest],a[i]
		max_heapify(a,largest)

def heap_extract_max(a):
	if len(a) is 0:
		return None
	m = a[0]
	a[0]=a[len(a)-1]
	a.pop()
	max_heapify(a,0)
	return m
	
def heap_increase_value(a, i, value):
	if a[i-1] > value:
		return None
	a[i-1] = value
	while i > 1 and a[int(i/2)] < a [i]:
		a[int(i/2)],a[i]=a[i],a[int(i/2)]
		i = i/2
		
def heap_insert(a,key):
	print(a)
	a.append(key)
	print(a)
	print(len(a)/2)
	i=int(len(a)/2)
	while i>0:
		max_heapify(a,i-1)
		i=int(i/2)
	

a=[9,6,5,0,8,2,7,1,3]
a=deque(a)
for i in range(int(len(a)/2))[::-1]:
	max_heapify(a,i)
print("Array after converting to heap :",a)
heap_insert(a,10)
print(a)





# heap_increase_value(a,1,100)
# print(a)
# print("The max value in the heap is : ", heap_extract_max(a))
# print(a)
# print("The max value in the heap is : ", heap_extract_max(a))
# print(a)
# print("The max value in the heap is : ", heap_extract_max(a))
# print(a)
# print("The max value in the heap is : ", heap_extract_max(a))
# print(a)
