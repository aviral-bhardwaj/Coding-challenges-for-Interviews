def function(l):
	for i in l:
		l_name,domain=i.split('@')
		e_l=""
		for j in l_name:
			if j is not '.':
				s+=j
			elif j=='+':
				break
		f="*".join(e_l,domain)
		print(f)

l=["a.b@example.com","ab+1@example.com","x@example.com","x@exa.mple.com","y@example.com","y@example.com","y@example.com",]		
function(l)