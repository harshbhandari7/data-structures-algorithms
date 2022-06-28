# Check whether a graph is Bipartite or not using DFS

from collections import defaultdict

class BipartiteGraph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.vertices = vertices
		self.colors = [-1] * self.vertices

	def add_edge(self, src, dest):
		self.graph[src].append(dest)

	def detect_bipartite(self, node):
		for neighbour in self.graph[node]:
			if self.colors[neighbour] == -1:
				self.colors[neighbour] = 1 - self.colors[node]
				if not self.detect_bipartite(neighbour):
					return False 
			elif self.colors[node] == self.colors[neighbour]:
				return False

		return True
		
	def traverse_graph(self):
		for i in range(1, self.vertices):
			if self.colors[i] == -1:
				self.colors[i] = 1
				if not self.detect_bipartite(i):
					return False

		return True 

if __name__ == '__main__':
	g = BipartiteGraph(9)

	g.add_edge(1, 2)
	g.add_edge(2, 1)
	g.add_edge(2, 3)
	g.add_edge(2, 6)
	g.add_edge(3, 2)
	g.add_edge(3, 4)
	g.add_edge(4, 3)
	g.add_edge(4, 5)
	g.add_edge(5, 4)
	g.add_edge(5, 6)
	g.add_edge(5, 7)
	g.add_edge(6, 2)
	g.add_edge(6, 5)
	g.add_edge(7, 5)
	g.add_edge(7, 8)
	g.add_edge(8, 7)


	# ------ Bipartite Graph -------
	# g.add_edge(1, 2)
	# g.add_edge(2, 1)
	# g.add_edge(2, 3)
	# g.add_edge(2, 5)
	# g.add_edge(3, 2)
	# g.add_edge(3, 4)
	# g.add_edge(4, 3)
	# g.add_edge(4, 5)
	# g.add_edge(5, 6)
	# g.add_edge(6, 5)
	
	print(g.traverse_graph())