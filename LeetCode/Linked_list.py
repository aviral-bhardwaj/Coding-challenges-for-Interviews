class Node:
	def __init__(self,value):
		self.data=value
		self.next=None

def insert(t,val):		
	tail.next=val
	return val

def print_(h):
	while h!=None:
		print(h.data)
		h=h.next
		
head=None
tail=None		
n=int(input("Numeber of elements ? "))
for i in range(n):
	if i==0:
		d=int(input())
		head=Node(d)
		tail=head
	else:
		tail=insert(tail,Node(int(input())))

head1=None
tail1=None		
m=int(input("Numeber of elements ? "))
for i in range(m):
	if i==0:
		d=int(input())
		head1=Node(d)
		tail1=head1
	else:
		tail1=insert(tail,Node(int(input())))

print("List 1 : ")		
print_(head)
print("List 2 : ")	
print_(head)