class Node:
	def __init__(self,val):
		self.left=None
		self.right=None
		self.data=val

def insert_node(root,node):		
	if root.data > node.data:
		if root.left is None:
			root.left = node
		else:
			insert_node(root.left,node)
	else:
		if root.right is None:
			root.right = node
		else:
			insert_node(root.right,node)
def height(root):
	if root is None:	
		return 0
	return 1+max(height(root.left),height(root.right))

def longest(r):
	if r is None:
		return 0
	lheight=height(r.left)
	rheight=height(r.right)
	ldiameter=longest(r.left)
	rdiameter=longest(r.right)
	return max(lheight+rheight+1,max(ldiameter,rdiameter))

	
def in_order(r):
	if r is None:
		return
	in_order(r.left)
	print(r.data)
	in_order(r.right)
	
l=[4,2,6,3,5,7,1,9]
r=Node(l[0])
for i in l[1:]:
	insert_node(r,Node(i))
in_order(r)
print("Height of the tree is : ",height(r))
print("The longest path in the tree is :  ",longest(r))
	