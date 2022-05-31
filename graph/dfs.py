from collections import defaultdict, deque

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.visited = set()

	def add_edge(self, src, dest):
		self.graph[src].append(dest)


	def dfs_traversal(self, node):
		if node not in self.visited:
			print(str(node), end=' ')
			self.visited.add(node)

			for neighbour in self.graph[node]:
				self.dfs_traversal(neighbour)

if __name__ == '__main__':
	g = Graph()
	g.add_edge(5, 3)
	g.add_edge(5, 7)
	g.add_edge(3, 2)
	g.add_edge(3, 4)
	g.add_edge(7, 8)
	g.add_edge(4, 8)
	
	
	# ----- DFS Traversal -----
	g.dfs_traversal(5)
	