'''
1.a Uninformed/Blind Search:
Uninformed search applies a way in which search tree is searched without any information about the search
space like initial state operators and test for the goal, so it is also called blind search.It examines each node
of the tree until it achieves the goal node.

Breadth-first Search:
o Breadth-first search is the most common search strategy for traversing a tree or graph. This algorithm
searches breadthwise in a tree or graph, so it is called breadth-first search.
o BFS algorithm starts searching from the root node of the tree and expands all successor node at the
current level before moving to nodes of next level.
o The breadth-first search algorithm is an example of a general-graph search algorithm.
o Breadth-first search implemented using FIFO queue data structure.

Advantages:
o BFS will provide a solution if any solution exists.
o If there are more than one solutions for a given problem, then BFS will provide the minimal solution
which requires the least number of steps.
Disadvantages:
o It requires lots of memory since each level of the tree must be saved into memory to expand the next
level.
o BFS needs lots of time if the solution is far away from the root node.
'''
# 1a. Write a Program to implement Uninformed search technique: BFS
from collections import defaultdict
# This class represents a graph using adjacency list representation
class Graph:
# Constructor
    def __init__(self):
# default dictionary to store graph
     self.graph = defaultdict(list)
# function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append((v))
        self.graph[v].append((u))
    def dispg(self):
        print(self.graph.items())
#Function to print a BFS of graph
    def BFS(self, s,goal):
# Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
# Create a queue for BFS
        frontier_q = []
# Mark the source node as visited and enqueue it
        frontier_q.append(s)
        visited[s] = True
        while frontier_q:
# Dequeue a vertex from queue and print it
            s = frontier_q.pop(0)
            print (s, end = " ")
        if(s == goal):
            print("\n Goal found")
        return
# Get all adjacent vertices of the dequeued vertex s.
#  # If adjacent hasnot beenvisited, then mark it visited and enqueue it
        for i in self.graph[s]:
            if visited[i] == False:
                frontier_q.append(i)
                visited[i] = True
                print("\n Goal not found")
# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(3,5)
g.dispg()
print ("Following is Breadth First Traversal (starting from vertex 1)")
g.BFS(1,4)

'''
OUTPUT:
dict_items([(0, [1, 3]), (1, [0, 2]), (3, [0, 2, 4, 5]), (2, [1, 3]), (4, [3, 5]), (5, [4,
3])])
Following is Breadth First Traversal (starting from vertex 1)
1
Goal not found
Goal not found
0
Goal not found
2 3
Goal not found
Goal not found
4
Goal found
'''