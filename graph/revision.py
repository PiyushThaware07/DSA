class Graph:
    def __init__(self):
        self.visited = []
        self.graph = []
        self.node_count = 0
    
    def add_vertices(self,value):
        if value in self.visited:
            print(f"node {value} already visited exists in node list visited")
            return
        else:
            self.node_count += 1
            self.visited.append(value)
            # add new column to graph
            for col in self.graph:
                col.append(0)
            # add new row to graph
            new_row = [0]*self.node_count
            self.graph.append(new_row)
            print(f"node {value} added")


