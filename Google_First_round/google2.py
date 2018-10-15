from collections import defaultdict

def function(l):
	max_c=-1
	i=0
	d=defaultdict(lambda:0)
	for (j,k) in enumerate(l):
		d[k]+=1
		#print(len(d))
		if len(d)>2:
			#print("here")
			if(j-i)>max_c:
				max_c=j-i
			while True:
				#print("in ",d)
				d[l[i]]-=1
				i+=1
				if d[l[i-1]]<=0:
					del d[l[i-1]]
					break
			#print("I here",i)
		#print(d)
	#print(max_c)
	return max_c
					


l1=[1,2,2,3,2,4,5,1,2]
l2=[1,2,1,3,4,3,4,5,1,2]
print(function(l1))
print(function(l2))