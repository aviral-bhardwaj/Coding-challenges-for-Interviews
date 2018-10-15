from collections import defaultdict

def function(l):
	d=defaultdict(lambda:0)
	for i in l:
		l_name,domain=i.split('@')
		e_l=""
		for j in l_name:
			if j=='+':
				break
			if j is not '.':
				e_l+=j
		f="@".join([e_l,domain])
		d[f]+=1
	c=0
	for i in d:	
		if d[i]>1:
			c+=1
	return c

#l=["a.b@example.com","ab+1@example.com","x@example.com","x@exa.mple.com","y@example.com","y@example.com","y@example.com"]		
l=[]
print(function(l))