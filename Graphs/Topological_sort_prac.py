from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph=defaultdict(list)
	
	def addEdge(self,u,v):
		self.graph[u].append(v)
		
	def topol(self):
		def topol_help(s):
			print(s)
			for i in self.graph[s]:
				in_degree[i]-=1
				if in_degree[i] is 0 and visited[i] is 0:
					topol_help(i)
					visited[i]=1
		in_degree=defaultdict(lambda: 0)
		visited={}
		for i in self.graph:
			visited[i]=0
			for j in self.graph[i]:
				if j not in self.graph:
					visited[j]=0
				in_degree[j]+=1
		for i in self.graph:
			if i not in in_degree:
				in_degree[i]=0
		for i in in_degree:
			if in_degree[i] is 0:
				topol_help(i)

		
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
