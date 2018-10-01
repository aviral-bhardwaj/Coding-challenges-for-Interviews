#Linear
def linear_search(l,se):
	for i in range(len(l)):
		if l[i]==int(se):
			return i+1
	return 0
	
l=[9,4,3,2,7,1,0,5,6,8]	
se=input("Enter the element to search : ")
f=linear_search(l,se)
if f:
	print("element found at : ",f)
else:
	print("element not found !")