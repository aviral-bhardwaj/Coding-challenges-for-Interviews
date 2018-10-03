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

def size_of_the_tree(r):
	if not r:
		return 0
	else:
		return 1+size_of_the_tree(r.l_child)+size_of_the_tree(r.r_child)

r=Node(5)
insert_node(r,Node(3))
insert_node(r,Node(10))
insert_node(r,Node(4))
insert_node(r,Node(16))
insert_node(r,Node(8))
insert_node(r,Node(18))
print("Elements in the BST are : ")
print_inorder(r)
print("Size of the tree is : ",size_of_the_tree(r))


		
		