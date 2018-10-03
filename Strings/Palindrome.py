def palindrome(s):
	b=0
	e=int(len(s)-1)
	for i in range(int(len(s)/2)):
		if s[b+i]!=s[e-i]:
			return "Not Palindrome"
	return "Palindrome"
str="chittiittiihc"
print(palindrome(str))