def max_wis(l):
	back={}
	n=len(l)
	
	def solution(i,l,back):
		if i<0:
			return []
		return solution(i-1,l,back) if back[i] else solution(i-2,l,back)+[l[i]]
	
	
	def top_down(l,i,best={-1:0,-2:0}):
		if i in best:
			return best[i]
		best[i]=max(top_down(l,i-1),top_down(l,i-2)+l[i])
		print(best)
		back[i]=best[i]==best[i-1]
		
		print(back)
		return best[i]
	
	return top_down(l,n-1),solution(n-1,l,back)


def max_wis1(l):
	if len(l) is 0:
		return 0
	else:
		return max(l[0]+max_wis1(l[2:]),max_wis1(l[1:]))

#print(max_wis([7,8,5]))
#print(max_wis([-1,8,10]))
#print(max_wis([-5, -1, -4]))

print(max_wis([1,2,3,4,2,5,7]))
print(max_wis1([1,2,3,4,2,5,7]))


