'''
Shortest distance between 2 nodes in a graph having
edges with unit weight using BFS.

'''

from collections import defaultdict, deque

class UndirectedGraph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)
		self.distance = [float('inf')] * self.vertices

	def add_edge(self, src, dest):
		self.graph[src].append(dest)

	def find_shortest_path(self, src):
		queue = deque([src])
		self.distance[src] = 0

		while queue:
			vertex = queue.popleft()
			current_distance = self.distance[vertex]

			for neighbour in self.graph[vertex]:
				if (self.distance[neighbour] == float('inf')) or (self.distance[neighbour] > current_distance + 1):
					self.distance[neighbour] = current_distance + 1
					queue.append(neighbour)

		print(f'Shortest Distance from Node {src} - ', self.distance)

if __name__ == '__main__':
	g = UndirectedGraph(9)

	g.add_edge(0, 1)
	g.add_edge(0, 3)
	g.add_edge(1, 0)
	g.add_edge(1, 2)
	g.add_edge(1, 3)
	g.add_edge(2, 1)
	g.add_edge(2, 6)
	g.add_edge(3, 0)
	g.add_edge(3, 1)
	g.add_edge(3, 4)
	g.add_edge(4, 3)
	g.add_edge(4, 5)
	g.add_edge(5, 4)
	g.add_edge(5, 6)
	g.add_edge(6, 2)
	g.add_edge(6, 5)
	g.add_edge(6, 7)
	g.add_edge(6, 8)
	g.add_edge(7, 6)
	g.add_edge(7, 8)
	g.add_edge(8, 6)
	g.add_edge(8, 7)

	g.find_shortest_path(0)


