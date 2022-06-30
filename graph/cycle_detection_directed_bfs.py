'''
	Cycle detection in a directed graph using BFS
	
	Cycle in a directed graph can be detected using Kahn's algorithm.
	As Kahn's Algo (Topological sort is applicable for only DAG's).

	So what we will do is we will try to sort the graph topologically,
	If it gets sorted topologically, It has NO cycle,
	If it doesn't, It has a cycle.
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

		node_ctr = 0
		while queue:
			vertex = queue.popleft()
			node_ctr += 1
			self.nodes_list.append(vertex)

			for neighbour in self.graph[vertex]:
				self.indegree[neighbour] -= 1

				if self.indegree[neighbour] == 0:
					queue.append(neighbour)

		# if vertices count node_ctr is equal, it means graph is traverserd and sorted topologically
		if self.vertices == node_ctr:
			return False

		return True


	def traverse_graph(self):
		return self.topological_sort()

if __name__ == '__main__':
	g = TopologicalSort(6)

	g.add_edge(2, 3)
	g.add_edge(3, 1)
	g.add_edge(4, 0)
	g.add_edge(4, 1)
	g.add_edge(5, 0)
	g.add_edge(5, 2)

	print('Does graph has cycle -', g.traverse_graph())