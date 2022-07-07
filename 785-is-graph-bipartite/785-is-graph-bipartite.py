from collections import defaultdict, deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        g = defaultdict(list)
        colors = [-1] * n
        
        for i in range(n):
            g[i] = graph[i]
            
        for i in range(n):
            if colors[i] == -1:
                q = deque([i])
                colors[i] = 1
                while q:
                    vertex = q.popleft()
                    for neighbour in g[vertex]:
                        if colors[neighbour] == -1:
                            colors[neighbour] = 1 - colors[vertex]
                            q.append(neighbour)
                        elif colors[neighbour] == colors[vertex]:
                            return False
                
        return True
        
        
        