class Node:
	def __init__(self,val):
		self.left=None
		self.right=None
		self.data=val

def build_tree(l):
	def build_tree_help(r,node):
		if r.data > node.data:
			if r.left is not None:
				build_tree_help(r.left,node)
			else:
				r.left=node
		elif r.data < node.data:
			if r.right is not None:
				build_tree_help(r.right,node)
			else:
				r.right=node

	if len(l) is not 0:
		r=Node(l[0])
		for i in l[1:]:
			build_tree_help(r,Node(i))
		return r

def search(r,se):		
	if r is None:
		return False
	if r.data > se:
		return search(r.left,se)
	elif r.data < se:
		return search(r.right,se)
	else:
		return True
		
def in_order(r):
	if r is None:
		return
	in_order(r.left)
	print(r.data)
	in_order(r.right)
	
l=[4,2,6,3,5,7,1,9]
root=build_tree(l)
#in_order(root)
e=int(input("Enter the element to search : "))
if search(root,e):
	print("Element found!")
else:
	print("Element not found!")


