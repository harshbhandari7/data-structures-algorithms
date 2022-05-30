# Graph representation list using Adjacency list

class AdjacentNode:
	def __init__(self, val):
		self.vertex = val
		self.next = None

class Graph:
	def __init__(self, no_of_vertices):
		# vertices -> no of vertex in graph
		self.vertices = no_of_vertices
		self.graph = [None] * self.vertices

	def add_edge(self, src, dest):
		# adding the node to the source node
		node = AdjacentNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		# adding the node to the destination node
		node = AdjacentNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node

	def print_graph(self):
		for i in range(self.vertices):
			print(f'Adjacent Nodes to vertex {i} ', end="")
			head = self.graph[i]
			while head:
				print(f'-> {head.vertex}', end="")
				head = head.next

			print()

if __name__ == "__main__":
	g = Graph(5)
	g.add_edge(0, 1)
	g.add_edge(0, 4)
	g.add_edge(1, 2)
	g.add_edge(1, 3)
	g.add_edge(1, 4)
	g.add_edge(2, 3)
	g.add_edge(3, 4)
	g.print_graph()

