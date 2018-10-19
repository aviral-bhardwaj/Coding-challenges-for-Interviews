class Queue:
	def __init__(self):
		self.queue=[]
		self.size=0
		self.msize=5
		[self.queue.append(None) for i in range(self.msize)]
		self.f=0
		self.r=0
	
	def enque(self,val):
		if self.size==self.msize:
			print("Queue is full!!")
		else:
			self.queue[self.r%self.msize]=val
			self.r+=1
			self.size+=1
	
	def deque(self):
		if self.size==0:
			print("Queue is Empty!!")
		else:
			rv=self.queue[self.f%self.msize]
			self.f+=1
			self.size-=1
			return rv
 
	
	def print_queue(self):
		for i in range(self.f,self.r):
			print(self.queue[i%self.msize])
	
		
if __name__=="__main__":
	queue=Queue()
	while(True):
		print("Enter element to push (press -1 to exit) : ")
		f=int(input())
		if f==-1:
			break
		else:
			queue.enque(f)
	while True:
		f=int(input("Enter choice (1. Enque 2. Deque 3. Print_queue 4. Exit) : "))
		if f==4:
			break
		elif f==1:
			queue.enque(int(input("Enter element to enque : ")))
		elif f==2:
			print(queue.deque())
		elif f==3:
			queue.print_queue()
		else:
			print("Enter the correct choice!!!")

	
	
	