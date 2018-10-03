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

def print_preorder(root):
	if root==None:
		return
	print(root.data)
	print_preorder(root.l_child)
	print_preorder(root.r_child)
def mirror_tree(r):
	if r==None:
		return 
	mirror_tree(r.l_child)
	mirror_tree(r.r_child)
	temp=r.l_child
	r.l_child=r.r_child
	r.r_child=temp
	
r=Node(4)
insert_node(r,Node(2))
insert_node(r,Node(6))
insert_node(r,Node(1))
insert_node(r,Node(3))
insert_node(r,Node(5))
insert_node(r,Node(7))
print("Elements in the BST before Mirroring are : ")
print_preorder(r)
mirror_tree(r)
print("Elements in the BST after Mirroring are : ")
print_preorder(r)

