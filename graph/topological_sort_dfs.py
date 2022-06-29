# Topological sort - Linear ordering of vertices such that  if there is an edge U -> V,
# U appears before V in that ordering.

# Topological sort is applicable only on Directed Acyclic Graph (DAG).

from collections import defaultdict, deque

class TopologicalSort:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.vertices = vertices
		self.visited = [0] * self.vertices
		self.stack = deque([])

	def add_edge(self, src, dest):
		self.graph[src].append(dest)

	def topological_sort(self, node):
		self.visited[node] = 1
		for neighbour in self.graph[node]:
			if not self.visited[neighbour]: 
				self.topological_sort(neighbour)

		self.stack.appendleft(node)

	def print_stack(self):
		for node in self.stack:
			print('->', node, end=" ")
		print()

	def traverse_graph(self):
		for i in range(self.vertices):
			if not self.visited[i]:
				self.topological_sort(i)

if __name__ == '__main__':
	g = TopologicalSort(6)

	g.add_edge(2, 3)
	g.add_edge(3, 1)
	g.add_edge(4, 0)
	g.add_edge(4, 1)
	g.add_edge(5, 0)
	g.add_edge(5, 2)

	g.traverse_graph()
	g.print_stack()