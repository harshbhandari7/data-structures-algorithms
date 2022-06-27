#  Cycle detection in a directed graph using DFS

from collections import defaultdict, deque

class CycleDetectDFS:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.vertices = vertices
		self.visited = [0] * (self.vertices + 1)
		self.dfs_visited = [0] * (self.vertices + 1)

	def add_edge(self, src, dest):
		self.graph[src].append(dest)
	
	def detect_cycle(self, node):
		self.visited[node] = 1
		self.dfs_visited[node] = 1

		for neighbour in self.graph[node]:
			if not self.visited[neighbour]:
				if self.detect_cycle(neighbour):
					return True
			elif self.dfs_visited[neighbour]:
				return True

		self.visited[node] = 0
		return False
	
	def has_cycle(self):
		for i in range(1, self.vertices+1):
			if not self.visited[i]:
				if self.detect_cycle(i):
					return True

		return False


if __name__ == '__main__':
	g = CycleDetectDFS(9)

	g.add_edge(1, 2)
	g.add_edge(2, 3)
	g.add_edge(3, 4)
	g.add_edge(3, 6)
	g.add_edge(4, 5)
	g.add_edge(6, 5)
	g.add_edge(7, 2)
	g.add_edge(7, 8)
	g.add_edge(8, 9)
	g.add_edge(9, 7)

	print(g.has_cycle())