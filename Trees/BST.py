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

for i in range(5):
	if i==0:
		r=Node(int(input("Enter the element to insert in BST : ")))
	else:
		d=int(input("Enter the element to insert in BST : "))
		insert_node(r,Node(d))
print_inorder(r)
		
		