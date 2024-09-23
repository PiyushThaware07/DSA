class Graph:
    def __init__(self):
        self.vertices = []
        self.graph = []
        self.node_count = 0
    
    def add_vertice(self,value):
        """Add a new vertex to the graph."""
        if value is self.add_vertice:
            print(f"{value} node is already present in node list")
            return
        else:
            self.node_count += 1
            self.vertices.append(value)
            # Add a column in each existing row for the new node
            for n in self.graph:
                n.append(0)
            # Add a new row for the new node, initialized to 0
            new_row = [0] * self.node_count
            self.graph.append(new_row)
            print(f"Node {value} added.")
    
    def add_edge(self,vertice1,vertice2):
        """Add an edge between two vertices."""
        if vertice1 not in self.vertices:
            print(f"{vertice1} node is not present in node list")
            return
        elif vertice2 not in self.vertices:
            print(f"{vertice2} node is not present in node list")
            return
        else:
            self.graph[self.vertices.index(vertice1)][self.vertices.index(vertice2)] = 1
            self.graph[self.vertices.index(vertice2)][self.vertices.index(vertice1)] = 1  # comment this line in case of directed graph or directed weighted graph
            print(f"Edge between {vertice1} and {vertice2} added.")
            return
    
    def print_graph(self):
        """Print the adjacency matrix of the graph."""
        print("Adjacency Matrix:")
        for row in range(self.node_count):
            for col in range(self.node_count):
                print(self.graph[row][col],end=" ")
            print()

# Usage example
g = Graph()
print("Before adding nodes")
print(g.vertices)
print(g.graph)

# Adding vertices
g.add_vertice("A")
g.add_vertice("B")
g.add_vertice("C")
g.add_vertice("D")

print("\nAfter adding nodes")
print(g.vertices)
g.print_graph()
g.add_edge("A","B")
g.add_edge("C","B")
g.print_graph()