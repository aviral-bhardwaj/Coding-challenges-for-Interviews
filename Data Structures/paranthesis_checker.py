from collections import deque

str=input("Enter the string to be checked : ")
stack=deque()
for i in str:
	print(i)
	if i=='(' or i=='{' or i=='[':
		stack.append(i)
	else:
		if i=='}' and stack[len(stack)-1]=='{':
			stack.pop()
		elif i==')' and stack[len(stack)-1]=='(':
			stack.pop()
		elif i==']' and stack[len(stack)-1]=='[':
			stack.pop()
		else:
			break

if len(stack)==0:
	print("Balanced")
else:
	print("Unbalanced")
			