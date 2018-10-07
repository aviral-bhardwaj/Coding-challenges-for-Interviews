from collections import defaultdict
from collections import deque

class Graph:
	def __init__(self):
		self.graph=defaultdict(list)
	
	def addEdge(self,u,v):
		self.graph[u].append(v)
	
	def BFS(self,s):
		visited=[False] * len(self.graph)
		print(visited)
		queue=deque()
		queue.append(s)
		visited[s]=True
		
		while queue:
			e=queue.popleft()
			print(queue,e)
			for i in self.graph[e]:
				if visited[i] is False:
					queue.append(i)
					visited[i]=True

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2) 
		