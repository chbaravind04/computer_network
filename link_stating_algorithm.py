import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def print_solution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def min_distance(self, dist, spt_set):
        min_distance = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if dist[v] < min_distance and not spt_set[v]:
                min_distance = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not spt_set[v]
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)


# Example usage
g = Graph(5)
g.graph = [
    [0, 9, 1, 0, 0],
    [9, 0, 4, 3, 0],
    [1, 4, 0, 8, 4],
    [0, 3, 8, 0, 2],
    [0, 0, 4, 2, 0]
]
g.dijkstra(0)
