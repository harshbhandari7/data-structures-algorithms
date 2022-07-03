'''
	Dijskstra Algorithm Implementation
	Shortest Path in Weighted Undirected Graphs
	
	Here we will use Priority Queue for implementing BFS to calculate shortest
	distances to adjacent nodes.

	This can be done using Queue also, but PQ optimizes the soln and makes less
	comparsion.

	In the soln, I have used PQ from queue module and its methods for implementation.
'''

from collections import defaultdict, deque
from queue import PriorityQueue

class Dijkstra:
	def __init__(self, v):
		self.vertices = v
		self.graph = defaultdict(list)
		self.distance = [float('inf')] * self.vertices

	def add_edge(self, src, dest, weight):
		self.graph[src].append((dest, weight))

	def find_shortest_path(self, src):
		priority_q = PriorityQueue()
		self.distance[src] = 0
		priority_q.put((0, src))

		while not priority_q.empty():
			vertex = priority_q.get() # vertex will be a tuple (distance, node)
			node = vertex[1]
			node_dist = vertex[0]

			for neighbour in self.graph[node]:
				adj_node = neighbour[0]
				adj_dist = neighbour[1]
				if (self.distance[adj_node] > node_dist + adj_dist):
					self.distance[adj_node] = node_dist + adj_dist
					priority_q.put((self.distance[adj_node], adj_node))

		print(f'Shortest Distance from source node as {src} ->', self.distance)


if __name__ == '__main__':
	g = Dijkstra(5)

	g.add_edge(0, 1, 2) # src, dest, weight
	g.add_edge(0, 3, 1)
	g.add_edge(1, 0, 2)
	g.add_edge(1, 2, 4)
	g.add_edge(1, 4, 5)
	g.add_edge(2, 1, 4)
	g.add_edge(2, 3, 3)
	g.add_edge(2, 4, 1)
	g.add_edge(3, 0, 1)
	g.add_edge(3, 2, 3)
	g.add_edge(4, 1, 5)
	g.add_edge(4, 2, 1)

	g.find_shortest_path(0)


	