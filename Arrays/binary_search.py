#Linear
def linear_search(l,left,right,se):
	mid=int((left+right)/2)
	if l[mid]==int(se):
		return mid+1
	else:
		if left>=right:
			return 0
		if l[mid]>int(se):
			return linear_search(l,left,mid-1,se)
		else:
			return linear_search(l,mid+1,right,se)
	
	
	
l=[9,4,3,2,7,1,0,5,6,8,23,45,234,123,45,7,57,56,3457,8,78,456,768]	
l.sort()
print(l)
se=input("Enter the element to search : ")
f=linear_search(l,0,len(l)-1,se)
if f:
	print("element found at : ",f)
else:
	print("element not found !")