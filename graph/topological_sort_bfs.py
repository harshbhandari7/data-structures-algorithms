'''
Topological sort - Linear ordering of vertices such that  if there is an edge U -> V,
U appears before V in that ordering.

Topological sort is applicable only on Directed Acyclic Graph (DAG).

kahn's Algorithm

In-degree of a node - No of incoming edges for a node.

'''
from collections import defaultdict, deque

class TopologicalSort:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)
		self.indegree = [0] * self.vertices
		self.nodes_list = deque([])

	def add_edge(self, src, dest):
		self.graph[src].append(dest)

	def topological_sort(self):
		# looping through all the nodes and their respective adjacent nodes to mark the indegree
		for node in range(self.vertices):
			for neighbour in self.graph[node]:
				self.indegree[neighbour] += 1

		# pushing all the nodes with indegree 0 in a queue
		# indegree 0 for a node means the node has no incoming edges
		queue = deque([])
		for i in range(self.vertices):
			if self.indegree[i] == 0:
				queue.append(i)

		while queue:
			vertex = queue.popleft()
			self.nodes_list.append(vertex)
			for neighbour in self.graph[vertex]:
				self.indegree[neighbour] -= 1

				if self.indegree[neighbour] == 0:
					queue.append(neighbour)

		for node in self.nodes_list:
			print('->', node, end=' ')

		print()


	def traverse_graph(self):
		self.topological_sort()

if __name__ == '__main__':
	g = TopologicalSort(6)

	g.add_edge(2, 3)
	g.add_edge(3, 1)
	g.add_edge(4, 0)
	g.add_edge(4, 1)
	g.add_edge(5, 0)
	g.add_edge(5, 2)

	g.traverse_graph()