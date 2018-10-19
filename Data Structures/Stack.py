class Stack:
	def __init__(self):
		self.stack=[]
		self.top=-1
		self.size=10
	
	def isEmpty(self):
		if self.top==-1:
			return True
		else:
			return False
	
	def push(self,val):
		if len(self.stack)<self.size:
			self.stack.append(val)
			self.top+=1
		else:
			print("Stack OverFlow!!")
	
	def pop(self):
		if self.isEmpty():
			return "Stack Underflow!!"
		else:
			self.top-=1
			return self.stack.pop()
			
	
	def peek(self):
		if self.isEmpty():
			return "Stack Underflow!!"
		else:
			return self.stack[self.top]
	def print_stack(self):
		return self.stack
			
if __name__=="__main__":
	stack=Stack()
	while(True):
		print("Enter element to insert (press -1 to exit) : ")
		f=int(input())
		if f==-1:
			break
		else:
			stack.push(f)
	while(True):
		print("Select the operation: 1. push 2. pop 3. peek 4. Check Stack 5. print_stack 6.exit : ")
		f=int(input())
		if f==1:
			stack.push(int(input("Enter the element to push : ")))
		elif f==2:
			print(stack.pop())
		elif f==3:
			print(stack.peek())
		elif f==4:
			print(stack.isEmpty())
		elif f==5:
			print(stack.print_stack())
		elif f==6:
			break
		else:
			print("Input invalid... select right option ... ")
		
		
		
		
		
		
		
		
	
	