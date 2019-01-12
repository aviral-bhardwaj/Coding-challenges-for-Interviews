def maxDiff(arr, n): 
    maxDiff = -1
    maxRight = arr[n - 1]  
    for i in range(n - 2, -1, -1): 
        if (arr[i] > maxRight): 
            maxRight = arr[i] 
        else: 
            diff = maxRight - arr[i] 
            if (diff > maxDiff): 
                maxDiff = diff 
    return maxDiff 

if __name__ == '__main__': 
    l=[7,9,5,6,3,2] 
    n = len(l) 
    print(maxDiff(l, n)) 
			


















			
				  
# def maxDifference(a):
	# l,r=0,len(a)-1
	# md=-1
	# while(l<r):
		# if a[l]<a[r]:
			# if a[l]<a[r] and md<abs(a[r]-a[l]):
				# md=abs(a[l]-a[r])
				# l+=1
			# elif a[r]<a[l]:
				# r-=1
			# else:
				# r-=1
		# else:
			# l+=1
	# return md

# l=[7,9,5,6,3,2]
# print(maxDifference(l))
