'''1b. Write a Program to implement  Uninformed search technique: 
DFS 
 
Depth-first Search 
o Depth-first search is a recursive algorithm for traversing a tree or graph data structure. 
o It is called the depth-first search because it starts from the root node and follows each path to its 
greatest depth node before moving to the next path. 
o DFS uses a stack data structure for its implementation. 
o The process of the DFS algorithm is similar to the BFS algorithm. 
 
Advantage: 
o DFS requires very less memory as it only needs to store a stack of the nodes on the path from root 
node to the current node. 
o It takes less time to reach to the goal node than BFS algorithm (if it traverses in the right path). 
Disadvantage: 
o There is the possibility that many states keep re-occurring, and there is no guarantee of finding the 
solution. 
o DFS algorithm goes for deep down searching and sometime it may go to the infinite loop. '''

# 1.b Write a Program to implement  Uninformed search technique: DFS 
 
from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    # The function to do DFS traversal. It uses recursive DFSUtil()
    def DFS(self):
        V = len(self.graph)  # total vertices

        # Mark all the vertices as not visited
        visited = [False] * V

        # Call the recursive helper function to print DFS traversal starting from all vertices one by one
        for i in range(V):
            if not visited[i]:
                self.DFSUtil(i, visited)

# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Depth First Traversal")
g.DFS() 
 
 
'''Output: 
 
Following is Depth First Traversal 
0 
3 
2 
1
 '''
 
 
 
 
 
 
