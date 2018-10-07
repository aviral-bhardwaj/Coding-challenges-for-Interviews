from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph=defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)
	
	def topol(self):
		def topolHelper(s):
			print(s)
			visited[s]=True
			for i in self.graph[s]:
				if visited[i] is not True:
					c[i]-=1
					if c[i] is 0:
						topolHelper(i)
		
		c=defaultdict(list)
		for i in self.graph:
			c[i]=0
		print(c)
		print(self.graph)
		for i in self.graph:
			for j in self.graph[i]:
				if j in c:
					c[j]+=1
				else:
					c[j]=1
		print(c)
		visited={}
		s=None
		for i in c:
			visited[i]=False
			if c[i] is 0:
				s=i
		
		topolHelper(s)

				
	
g=Graph()
g.addEdge(1,2)
g.addEdge(1,7)
g.addEdge(1,6)
g.addEdge(2,3)
g.addEdge(2,5)
g.addEdge(3,7)
g.addEdge(4,3)
g.addEdge(5,4)
g.addEdge(6,4)
g.addEdge(8,1)

g.topol()


