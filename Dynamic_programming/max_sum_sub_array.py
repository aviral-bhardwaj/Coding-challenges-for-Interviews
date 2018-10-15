def max_sum_sub_array(l):
	max_sum_so_far=None
	cur_sum=None
	index=None
	for i in range(len(l)):
		if cur_sum is not None:
			cur_sum+=l[i]
			if cur_sum<0:
				cur_sum=0
			if max_sum_so_far is None or cur_sum>max_sum_so_far:
				max_sum_so_far=cur_sum
				index=i
		else:
			cur_sum=l[i]
			if cur_sum<0:
				cur_sum=0
			if max_sum_so_far is None or cur_sum>max_sum_so_far:
				max_sum_so_far=cur_sum
				index=i
	res=[]
	sum=0
	while index>=0:
		sum+=l[index]
		res.append(l[index])
		index-=1
		if sum==max_sum_so_far:
			break
	print(res[::-1],max_sum_so_far)

#l=[int(i) for i in input().split()]
l=[10,-5,-3,4,2,12,-8,-12,19]
#l=[-3,10,5,-20,4,11,-5,7]
max_sum_sub_array(l)