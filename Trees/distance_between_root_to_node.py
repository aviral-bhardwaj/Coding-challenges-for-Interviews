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

def distance(root,path,p):
	if root is None:
		return False
	path.append(root.data)
	if root.data is p:
		return True
	if ((root.l_child is not None and distance(root.l_child,path,p)) or (root.r_child is not None and distance(root.r_child,path,p))):
		return True
	path.pop()
	return False
	
	
	
r=Node(5)
insert_node(r,Node(3))
insert_node(r,Node(10))
insert_node(r,Node(4))
insert_node(r,Node(16))
insert_node(r,Node(8))
insert_node(r,Node(18))
print("Elements in the first BST are : ")
print_inorder(r)
p=int(input("Enter two nodes to find the distance: "))
path=[]
distance(r,path,p)
print("The  distance betweens two diven nodes: ",path)