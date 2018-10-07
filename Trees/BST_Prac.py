class Node:
	def __init__(self,val):
		self.left=None
		self.right=None
		self.data=val

def insert_node(r,node):
	if r is None:
		r=node
	if r.data > node.data:
		if r.left is None:
			r.left=node
		else:
			insert_node(r.left,node)
	else:
		if r.right is None:
			r.right=node
		else:
			insert_node(r.right,node)

def find_path(r,path,val):
	if r is None:
		return
	if r.data is val:
		path.append(r.data)
		return
	path.append(r.data)
	if r.data>val:
		find_path(r.left,path,val)
	else:
		find_path(r.right,path,val)

def LCA(path,path1):
	if len(path)<len(path1):
		k=path 
	else:
		k=path1		
	for i in range(min(len(path),len(path1))):
		if path[i]!=path1[i]:
			return path[i-1]
	return k[-1]	

def in_order(r):
	if r is None:
		return
	in_order(r.left)
	print(r.data)
	in_order(r.right)

def LCA_recur(r,n1,n2):
	if r is None:
		return 
	if r.data>n1 and r.data>n2:
		return LCA_recur(r.left,n1,n2)
	elif r.data<n1 and r.data<n2:
		return LCA_recur(r.right,n1,n2)
	return r.data

def no_of_nodes(r):
	if r is None:
		return 0
	else:
		return 1+no_of_nodes(r.left)+no_of_nodes(r.right)

def min_bst(r):
	if r is None:
		return
	if r.left is None:
		return r.data
	else:
		return min_bst(r.left)
def max_bst(r):
	if r is None:
		return
	if r.right is None:
		return r.data
	else:
		return max_bst(r.right)
	
def no_of_leaves(r,c):
	if r is None:
		return 
	if r.left is None and r.right is None:
		c[0]+=1
	no_of_leaves(r.left,c)
	no_of_leaves(r.right,c)
def no_of_fullNodes(r,f):
	if r is None:
		return 
	if r.left is not None and r.right is not None:
		f[0]+=1
	no_of_fullNodes(r.left,f)
	no_of_fullNodes(r.right,f)
def height(r):
	if r is None:
		return 0
	return 1+max(height(r.left) if r.left is not None else 0,height(r.right) if r.right is not None else 0)
def minValueNode(node):
	c=node
	while c.left is not None:
		c=c.left
	return c
	
def delete_node(r,k):
	if r is None:	
		return r
	if r.data > k:
		r.left=delete_node(r.left,k)
	elif r.data < k:
		r.right=delete_node(r.right,k)
	else:
		if r.left is None:
			temp=r.right
			r=None
			return temp
		elif r.right is None:
			temp=r.left
			r=None
			return temp
		temp=minValueNode(r.right)
		r.data=temp.data
		r.right=delete_node(r.right,temp.data)
	return r

def diameter_of_tree(r):
	if r is None:
		return 0
	lheight=height(r.left)
	rheight=height(r.right)
	
	ldiameter=diameter_of_tree(r.left)
	rdiameter=diameter_of_tree(r.right)
	
	return max(lheight+rheight+1,max(ldiameter,rdiameter))
	
	
l=[4,2,6,1,3,5,7,8,9]
r=Node(l[0])
for i in l[1:]:
	insert_node(r,Node(i))
in_order(r)
print("After deleting node 5 tree is as below : ")
delete_node(r,9)
in_order(r)
#print(diameter_of_tree(r))
print("The height of the tree is : ",height(r))
























# delete_node(r,5)
# print("Number of nodes in BST: ",no_of_nodes(r))
# print("Min element in the BST : ",min_bst(r))
# print("Max element in the BST : ",max_bst(r))
# c=[0]
# no_of_leaves(r,c)
# print("No of leaf nodes : ",c[0])
# f=[0]
# no_of_fullNodes(r,f)
# print("No of full nodes : ",f[0])
#path=[]
#find_path(r,path,int(input()))
#print(path)
#path1=[]
#find_path(r,path1,int(input()))
#print(path1)
#print("LCA : ",LCA(path,path1))
#print("LCA Recursion : ",LCA_recur(r,int(input()),int(input())))






















