






s=input()
l=[]
for i in range(len(s)+1):
	for j in range((len(s)-i)+1):
		if len(s[j:j+i])>0:
			l.append((s[j:j+i]))
print(l)