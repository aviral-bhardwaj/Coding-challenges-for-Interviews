def function(s):
	i=len(s)-1
	res=""
	while i>=0:
		n=None
		if s[i]=='1':
			n=s[i-2:i+1][::-1]
			res+=chr(int(n))
			i-=3
		elif s[i]=='3' or s[i]=='6' or s[i]=='7' or s[i]=='8' or s[i]=='9':
			n=s[i-1:i+1][::-1]
			res+=chr(int(n))
			i-=2
	for i in res:
		for j in i:
			print(j,end='')
		print()


str="23511011501782351112179911801562340161171141148"
print(function(str))