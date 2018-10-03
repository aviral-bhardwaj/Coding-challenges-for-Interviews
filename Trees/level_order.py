from collections import deque
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

def level_order(r):
	qu=deque()
	qu.append(r)
	while qu:
		node=qu.popleft()
		if not node:
			return
		print(node.data,end=" ")
		qu.append(node.l_child)
		qu.append(node.r_child)

	
r=Node(4)
insert_node(r,Node(2))
insert_node(r,Node(6))
insert_node(r,Node(1))
insert_node(r,Node(3))
insert_node(r,Node(5))
insert_node(r,Node(7))
print_inorder(r)
print()
print("Printing Elements in Level Order ")
level_order(r)





