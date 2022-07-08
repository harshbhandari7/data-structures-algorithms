'''
	Floyd warshall implementation

	Floyd-Warshall, computes the shortest distances between every pair of vertices
	in the graph.
'''

class FloydWarshall:
	def __init__(self, v):
		self.vertices = v
		self.graph = []
		self.distance = []

	def add_edge(self, edge_weights):
		self.graph.append(edge_weights)

	def traverse_graph(self):
		self.distance = self.graph.copy()

		for k in range(self.vertices):
			for i in range(self.vertices):
				for j in range(self.vertices):
					if self.distance[i][j] > (self.distance[i][k] + self.distance[k][j]):
						self.distance[i][j] = self.distance[i][k] + self.distance[k][j]

		print('Shortest distance between each pair of vertices - ', self.distance)

if __name__ == '__main__':
	INF  = float('inf')

	g = FloydWarshall(4)

	g.add_edge([0, 5, INF, 10])
	g.add_edge([INF, 0, 3, INF])
	g.add_edge([INF, INF, 0, 1])
	g.add_edge([INF, INF, INF, 0])

	g.traverse_graph()
