from collections import defaultdict
class Node:
	def __init__(self,val):
		self.next=None
		self.val=val

def insert_node(h,val):
	while h.next!=None:
		h=h.next
	h.next=Node(val)

def print_nodes(h):
	while h is not None:
		print(h.val,end=" ")
		h=h.next

def delete_node(h,val):
	while h is not None:
		if h.val==val:
			break
		p=h
		h=h.next
	p.next=h.next

def make_circular(h):
	temp=h
	while h.next is not None:
		h=h.next
	h.next=temp

def print_circular(h):
	d=defaultdict(lambda:0)
	while h not in d:
		d[h]+=1
		print(h.val)
		h=h.next
	print(d)
		
		
	
	
l=[5,3,7,1,9,3,10]
head=Node(l[0])

for i in l[1:]:
	insert_node(head,i)
	
print_nodes(head)
print()
delete_node(head,int(input("Enter element to remove: ")))
print("Element after removal : ",end=" ")
print_nodes(head)	
make_circular(head)
print()
print_circular(head)