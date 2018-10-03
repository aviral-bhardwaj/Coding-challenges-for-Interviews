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
	
def height(root):
	if root is None:
		return 0
	return 1+max(height(root.l_child),height(root.r_child))
	
def Diameter_of_tree(root):
	if root is None:
		return 0
	lheight=height(root.l_child)
	rheight=height(root.r_child)
	ldiameter = Diameter_of_tree(root.l_child)
	rdiameter = Diameter_of_tree(root.r_child)
	return max(lheight+rheight+1,max(ldiameter,rdiameter))
	
	
	
r=Node(4)
insert_node(r,Node(2))
insert_node(r,Node(6))
insert_node(r,Node(1))
insert_node(r,Node(3))
insert_node(r,Node(5))
insert_node(r,Node(7))
insert_node(r,Node(8))
insert_node(r,Node(9))
insert_node(r,Node(0))

print("The Diameter of the tree is : ",Diameter_of_tree(r))
