class DistanceVectorRouting:
    def __init__(self, nodes, graph):
        self.nodes = nodes
        self.graph = graph
        self.routing_table = {}

    def initialize_routing_table(self, source_node):
        for node in self.nodes:
            if node == source_node:
                self.routing_table[node] = {'distance': 0, 'next_hop': node}
            else:
                self.routing_table[node] = {'distance': float('inf'), 'next_hop': None}

    def update_routing_table(self):
        for node in self.nodes:
            min_distance = float('inf')
            next_hop = None
            for neighbor in self.graph[node]:
                distance = self.routing_table[neighbor]['distance'] + self.graph[node][neighbor]
                if distance < min_distance:
                    min_distance = distance
                    next_hop = neighbor
            if min_distance < self.routing_table[node]['distance']:
                self.routing_table[node]['distance'] = min_distance
                self.routing_table[node]['next_hop'] = next_hop

    def print_routing_table(self):
        print("Routing Table:")
        print("-----------------")
        print("Node\tDistance\tNext Hop")
        for node in self.nodes:
            print(f"{node}\t{self.routing_table[node]['distance']}\t\t{self.routing_table[node]['next_hop']}")
        print("-----------------")

# Example usage
nodes = ['A', 'B', 'C', 'D', 'E']
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 3, 'D': 1},
    'C': {'A': 1, 'B': 3, 'D': 4},
    'D': {'B': 1, 'C': 4, 'E': 2},
    'E': {'D': 2}
}

routing = DistanceVectorRouting(nodes, graph)
source_node = 'A'
routing.initialize_routing_table(source_node)
routing.print_routing_table()

for _ in range(len(nodes) - 1):
    routing.update_routing_table()

routing.print_routing_table()
