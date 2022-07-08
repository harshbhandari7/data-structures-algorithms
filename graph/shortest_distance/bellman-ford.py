'''
	For a graph having negative edges, dijkstra won't work.

 	Bellman ford algo can be used to find the shortest path when there are negative edges.

 	- The graph must be directed.
 	- For undirected, we can convert it to direct and apply the algo.
 	- This algo can also be used to detect the negative cycle.

'''

class BellmanFord:
	def __init__(self, v):
		self.vertices = v
		self.graph = []
		self.distance = [ float('inf') ] * self.vertices

	def add_edge(self, src, dest, weight):
		self.graph.append((src, dest, weight))

	def traverse_graph(self, src):
		self.distance[src] = 0

		# relaxing all the edges n-1 times (n = no of vertices)
		for i in range(self.vertices - 1):
			for node in self.graph:
				u = node[0]
				v = node[1]
				w = node[2]

				if self.distance[u] + w < self.distance[v]:
					self.distance[v] = self.distance[u] + w

		# relaxing in 1 more time to detect whether the graph has -ve cycle or not.
		# if distance reduces it means it has a negative cycle.

		is_cycle = False

		for node in self.graph:
			u = node[0]
			v = node[1]
			w = node[2]

			if self.distance[u] + w < self.distance[v]:
				is_cycle = True
				break


		if is_cycle:
			print('The Graph has a negative weight cycle')
		else:
			print(f'Shortest distance from Node {src} - ', self.distance)

if __name__ == '__main__':
	g = BellmanFord(6)

	# Graph with no cycle

	# g.add_edge(0, 1, 5) # src, dest. weight
	# g.add_edge(1, 2, -2)
	# g.add_edge(2, 4, 3)
	# g.add_edge(1, 5, -3)
	# g.add_edge(5, 3, 1)
	# g.add_edge(3, 2, 6)
	# g.add_edge(3, 4, -2)

	# Graph having negative cycle

	g.add_edge(0, 1, 5)
	g.add_edge(0, 4, 2)
	g.add_edge(4, 5, 4)
	g.add_edge(1, 2, 2)
	g.add_edge(2, 3, -8)
	g.add_edge(3, 1, 4)

	g.traverse_graph(0)