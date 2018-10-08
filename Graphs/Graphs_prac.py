from collections import defaultdict
from collections import deque
class Graph:
	def __init__(self):
		self.graph=defaultdict(list)
		
	def addEdge(self,u,v):
		self.graph[u].append(v)
	
	def BFS(self,s):
		visited={}
		for i in self.graph.keys():
			visited[i]=False
		if s not in self.graph:
			return None
		q=deque([])
		q.append(s)
		visited[s]=True
		while len(q) is not 0:
			ce=q.popleft()
			print(ce)
			for i in self.graph[ce]:
				if visited[i] is False:
					visited[i]=True
					q.append(i)
	def keys(self):
		return self.graph.keys()
	
	def DFS(self,s,visited):
		if visited[s] is True:
			return
		visited[s]=True
		for i in self.graph[s]:
			if visited[i] is False:
				self.DFS(i,visited)
		print(s)
	
		
graph=Graph()
graph.addEdge(0,1)
graph.addEdge(1,2)
graph.addEdge(0,2)
graph.addEdge(2,0)
graph.addEdge(2,3)
graph.addEdge(3,3)

print("Elements order in BFS: ")
graph.BFS(2)
print("Elements order in BFS: ")
graph.BFS(1)
print()
visited={}
for i in graph.keys():
	visited[i]=False
print("Elements order in DFS with 2 as source: ")
graph.DFS(2,visited)
for i in graph.keys():
	visited[i]=False
print("Elements order in DFS with 1 as source: ")
graph.DFS(1,visited)



