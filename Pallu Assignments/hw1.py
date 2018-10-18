def permu(xs):
	if xs:
		r,h=[],[]
		for x in xs:
			if x not in h:
				ts=xs[:]
				ts.remove(x)
				for p in permu(ts):
					r.append([x]+p)
			h.append(x)
		return r
	else:
		return [[]]


print(permu(['a','b','c']))

