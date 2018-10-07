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

def distance_from_root(root,path1,p):
	if root is None:
		return False
	path1.append(root)
	if root.data is p:
		return True
	if((root.l_child!=None and distance_from_root(root.l_child,path1,p)) or (root.r_child!=None and distance_from_root(root.r_child,path1,p))):
		return True
	path1.pop()
	return False
	
	
def distance(root,p,q):	
	if root is not None:
		path1=[]
		path2=[]
		distance_from_root(r,path1,p)
		distance_from_root(r,path2,q)
		path1,path2=[i.data for i in path1], [i.data for i in path2]
		i=0
		while i<len(path1) and i<len(path2):
			if path1[i]!=path2[i]:
				break
			i+=1
			
		return len(path1)+len(path2)-2*i
	else:
		return 0
	
	
r=Node(5)
insert_node(r,Node(3))
insert_node(r,Node(10))
insert_node(r,Node(4))
insert_node(r,Node(16))
insert_node(r,Node(8))
insert_node(r,Node(18))
print("Elements in the first BST are : ")
print_inorder(r)
p,q=[int(i) for i in input("Enter two nodes to find the distance: ").split()]
print("The  distance betweens two diven nodes: ",distance(r,p,q))





