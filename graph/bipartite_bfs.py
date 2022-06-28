# A Bipartite graph is graph that can be coloured using 2 colors such that
# no two adjacent have same color.

# if a graph has ODD length cycle it's NOT a Bipartite.

from collections import defaultdict, deque

class BipartiteGraph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.vertices = vertices
		self.colors = [-1] * self.vertices

	def add_edge(self, src, dest):
		self.graph[src].append(dest)

	def detect_bipartite(self, node):
		queue = deque([node])
		self.colors[node] = 1

		while queue:
			vertex = queue.popleft()

			for neighbour in self.graph[vertex]:
				if self.colors[neighbour] == -1:
					self.colors[neighbour] = 1 - self.colors[vertex]
				elif self.colors[node] == self.colors[neighbour]:
					return False

		return True

	def traverse_graph(self):
		for i in range(self.vertices):
			if self.colors[i] == -1:
				if not self.detect_bipartite(i):
					return False

		return True

if __name__ == '__main__':
	g = BipartiteGraph(8)

	g.add_edge(0, 1)
	g.add_edge(1, 2)
	g.add_edge(1, 7)
	g.add_edge(2, 3)
	g.add_edge(7, 4)
	g.add_edge(3, 4)
	g.add_edge(4, 5)
	g.add_edge(5, 6)

	print(g.traverse_graph())