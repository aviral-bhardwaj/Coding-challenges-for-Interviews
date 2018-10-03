class Node:
	def __init__(self,val):
		self.l_child=None
		self.r_child=None
		self.data=val

def insert_node(root,node):
	if root is None:
		root=node
	else:
		if root.data > node.data:
			if root.l_child is None:
				root.l_child=node
			else:
				insert_node(root.l_child,node)
		else:
			if root.r_child is None:
				root.r_child=node
			else:
				insert_node(root.r_child,node)

def print_inorder(root):
	if root==None:
		return
	print_inorder(root.l_child)
	print(root.data)
	print_inorder(root.r_child)

def check_identity(r,r1):
	if r==None and r1==None:
		return 1
	if r != None and r1!=None and r.data==r1.data:
		ltree=check_identity(r.l_child,r1.l_child)
		if ltree is 0:
			return 0
		rtree=check_identity(r.r_child,r1.r_child)
		if rtree is 0:
			return 0
	else:
		return 0
	return 1
	
r=Node(5)
insert_node(r,Node(3))
insert_node(r,Node(10))
insert_node(r,Node(4))
insert_node(r,Node(16))
insert_node(r,Node(8))
insert_node(r,Node(18))
print("Elements in the first BST are : ")
print_inorder(r)

r1=Node(5)
insert_node(r1,Node(3))
insert_node(r1,Node(10))
insert_node(r1,Node(4))
insert_node(r1,Node(16))
insert_node(r1,Node(80))
insert_node(r1,Node(18))

print("Elements in the second BST are : ")
print_inorder(r1)

if check_identity(r,r1):
	print("Two trees are identical ...")
else:
	print("Two trees are not identical...!")
