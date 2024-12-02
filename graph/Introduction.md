# GRAPH : It is also an non-linear data structure

G = (V,E)
where : G -> Graph 
        V -> Set of vertices
        E -> Set of edges

() -> Ordered pairs
{} ->Unordered pairs


1. Factor
* If direction of graph is mentioned then it is a directed graph.all edges are bidirectional.
* If direction of graph is not mentioned then it is a undirected graph.all edges are unidirectional.
  ![alt text](https://i.sstatic.net/5xkVt.png)


2. Factor
* Weighted Graph -> A graph in which each edge is assigned with some weigth , cost, or value or it can be anything.
* Unweighted Graph -> A graph in which edges dont have any values then it is unweighted graph.
  ![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNGXHHiUcXTULCnbVB1y6KWYfIZTWAViNk5w&s)


3. Factor
* Cyclic Graph -> A graph which have cycle is a cyclic graph.
* Acyclic Graph -> A graph which dont have an cycle is an acyclic graph.
  ![alt text](https://afteracademy.com/images/introduction-to-graph-in-programming-cyclic-acyclic-graph-5ff471a71f3b0a58.png)


## Basic Graph Terminology :
1. Degree : 
   * Degree of a Vertex: The number of edges connected to a vertex.
   * In-Degree (Directed Graph): Number of incoming edges.
   * Out-Degree (Directed Graph): Number of outgoing edges.


2. Path : A sequence of vertices connected by edges.
   * Simple Path: No vertex is repeated.
   * Cycle: A path that starts and ends at the same vertex.
   * length of path should be always equal to or greater than 1.


3. Connected Graph : A graph is connected if there is a path between any two vertices.


4. Degree of Graph
   * Regular Graph: All vertices have the same degree.
   * Complete Graph: Every pair of vertices is connected by an edge.

5. Graph Representation : 
   * Adjacency Matrix : 
    ![alt text](https://studyglance.in/ds/images/Adjacency-Matrix.jpg)
     1. Create k X k matrix.
     2. Row and Column represents the node of graph
     3. if edge is present then store 1 otherwise stre 0.

   * Adjacency List : 
    ![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20231130131603/Graph-Representation-of-Undirected-graph-to-Adjacency-List.png)