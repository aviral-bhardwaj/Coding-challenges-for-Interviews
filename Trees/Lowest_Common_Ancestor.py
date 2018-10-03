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
	print(root.data,end=" ")
	print_inorder(root.r_child)

def LCA(r,p,q):
	if not r:
		return None
	if r.data>p and r.data>q:
		return LCA(r.l_child,p,q)
	if r.data<p and r.data<q:
		return LCA(r.r_child,p,q)
	return r
	
	
	
r=Node(4)
insert_node(r,Node(2))
insert_node(r,Node(6))
insert_node(r,Node(1))
insert_node(r,Node(3))
insert_node(r,Node(5))
insert_node(r,Node(7))
p=int(input("Enter n1 :" ))
q=int(input("Enter n2 :" ))
print("Lowest Common Ancestor is : ",LCA(r,p,q).data)
