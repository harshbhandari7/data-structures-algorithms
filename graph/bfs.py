from collections import defaultdict, deque

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, src, dest):
		self.graph[src].append(dest)


	def bfs_traversal(self, node):
		visited = set()
		queue = deque([node])
		visited.add(node)

		while queue:

			# dequeue vertex from queue
			vertex = queue.popleft()
			print(str(vertex), end=' ')

			for neighbour in self.graph[vertex]:
				if neighbour not in visited:
					visited.add(neighbour)
					queue.append(neighbour)

if __name__ == '__main__':
	g = Graph()
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(2, 5)
	g.add_edge(5, 5)
	
	# ----- BFS Traversal -----
	g.bfs_traversal(0)
	