# Cycle detections using dfs

from collections import defaultdict, deque

class CycleDetectDFS:
	def __init__(self):
		self.graph = defaultdict(list)
		self.visited = set()

	def add_edge(self, src, dest):
		self.graph[src].append(dest)

	def detect_cycle(self, node, parent_node):
		if node not in self.visited:
			self.visited.add(node)

			for neighbour in self.graph[node]:
				if neighbour not in self.visited:
					if self.detect_cycle(neighbour, node):
						return True
				elif neighbour != parent_node and neighbour in self.visited:
					return True

		return False

if __name__ == '__main__':
	g = CycleDetectDFS()
	# g.add_edge(2, 5)
	# g.add_edge(5, 2)
	# g.add_edge(5, 6)
	# g.add_edge(5, 8)
	# g.add_edge(6, 5)
	# g.add_edge(6, 7)
	# g.add_edge(7, 6)
	# g.add_edge(7, 8)
	# g.add_edge(8, 7)
	# g.add_edge(8, 5)
	
	# calling detect cycle method on 2nd node, -1 signifies that it doesn't have parent
	is_cycle = g.detect_cycle(2, -1)
	print('Does Graph has Cycle ? -', is_cycle)
	