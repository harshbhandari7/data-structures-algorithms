'''
	Shortest distance in a directed acyclic graph using Topological sort(DFS) and BFS
'''

from collections import defaultdict, deque

class WeightedDAG:
	def __init__(self, v):
		self.vertices = v
		self.graph = defaultdict(list)
		self.visited = [0] * self.vertices
		self.distance = [float('inf')] * self.vertices
		self.topo_order = deque([])

	def add_edge(self, src, dest, weight):
		self.graph[src].append((dest, weight))

	def topological_sort(self, node):
		self.visited[node] = 1
		for neighbour in self.graph[node]:
			if not self.visited[neighbour[0]]:
				self.topological_sort(neighbour[0])

		self.topo_order.appendleft(node)

	def print_topo_order(self):
		print('Topological Sort Order', end=" ")
		for node in self.topo_order:
			print('->', node, end="")

		print()

	def traverse_graph(self):
		for i in range(self.vertices):
			if not self.visited[i]:
				self.topological_sort(i)

	def find_shortest_path(self, src):
		self.distance[src] = 0

		while self.topo_order:
			node = self.topo_order.popleft()

			if self.distance[node] != float('inf'):
				for neighbour in self.graph[node]:
					if self.distance[neighbour[0]] > self.distance[node] + neighbour[1]:
							self.distance[neighbour[0]] = self.distance[node] + neighbour[1]

		print('Shortest Distance->', self.distance)

if __name__ == '__main__':
	g = WeightedDAG(6)

	g.add_edge(0, 1, 2) # src, dest, weight
	g.add_edge(0, 4, 1)
	g.add_edge(1, 2, 3)
	g.add_edge(2, 3, 6)
	g.add_edge(4, 2, 2)
	g.add_edge(4, 5, 4)
	g.add_edge(5, 3, 1)

	# travering through the entire graph (graph could have multiple components)
	g.traverse_graph()

	# now the graph is sorted in topological order and
	# stored in topo_order, we will find shortest distance by traversing
	# through this topo_order.

	g.print_topo_order()

	# calling method to calculate shortest distance

	g.find_shortest_path(0)