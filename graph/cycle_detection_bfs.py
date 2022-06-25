from collections import defaultdict, deque

class CycleDetectBFS:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, src, dest):
		self.graph[src].append(dest)

	def detect_cycle(self, node):
		visited = set()
		queue = deque([(node, -1)])
		visited.add(node)

		while queue:
			vertex_tuple = queue.popleft()

			for neighbour in self.graph[vertex_tuple[0]]:

				if neighbour != vertex_tuple[1] and neighbour in visited:
					return True

				if neighbour not in visited:
					queue.append((neighbour, vertex_tuple[0]))
					visited.add(neighbour)

		return False

if __name__ == '__main__':
	g = CycleDetectBFS()

	g.add_edge(3, 5)
	g.add_edge(5, 6)
	g.add_edge(5, 10)
	g.add_edge(6, 5)
	g.add_edge(6, 7)
	g.add_edge(7, 6)
	g.add_edge(7, 8)
	g.add_edge(8, 9)
	g.add_edge(8, 11)
	g.add_edge(9, 8)
	g.add_edge(9, 10)
	g.add_edge(10, 5)
	g.add_edge(10, 9)
	g.add_edge(11, 8)

	print(g.detect_cycle(3))

	# g.add_edge(1, 2)
	# g.add_edge(2, 1)
	# g.add_edge(2, 4)
	# g.add_edge(4, 2)

	# print(g.detect_cycle(1))