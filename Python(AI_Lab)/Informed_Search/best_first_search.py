'''2. Informed Search Algorithms 
 
Informed search algorithm contains an array of knowledge such as how far we are from the goal, path cost, 
how to reach to goal node, etc. This knowledge help agents to explore less to the search space and find more 
efficiently the goal node. 
The informed search algorithm is more useful for large search space. Informed search algorithm uses the 
idea of heuristic, so it is also called Heuristic search. 
Heuristics function: 
It takes the current state of the agent as its input and produces the estimation of how close agent is from the 
goal. The heuristic method, however, might not always give the best solution, but it guaranteed to find a 
good solution in reasonable time. Heuristic function estimates how close a state is to the goal. It is 
represented by h(n), and it calculates the cost of an optimal path between the pair of states. The value of the 
heuristic function is always positive. 
Best-first Search Algorithm (Greedy Search): 
Greedy best-first search algorithm always selects the path which appears best at that moment. It is the 
combination of depth-first search and breadth-first search algorithms. It uses the heuristic function and 
search. 
Best first search algorithm: 
Step 1: Place the starting node into the OPEN list. 
Step 2: If the OPEN list is empty, Stop and return failure. 
                       Step 3: Remove the node n, from the OPEN list which has the lowest value of h(n), and places it in 
the CLOSED list. 
Step 4: Expand the node n, and generate the successors of node n. 
Step 5: Check each successor of node n, and find whether any node is a goal node or not. If any 
successor node is goal node, then return success and terminate the search, else proceed to Step 6. 
Step 6: For each successor node, algorithm checks for evaluation function f(n), and then check if the 
node has been in either OPEN or CLOSED list. If the node has not been in both list, then add it to the 
OPEN list. 
Step 7: Return to Step 2.

Advantages: 
o Best first search can switch between BFS and DFS by gaining the advantages of both the algorithms. 
o This algorithm is more efficient than BFS and DFS algorithms. 
Disadvantages: 
o It can behave as an unguided depth-first search in the worst case scenario. 
o It can get stuck in a loop as DFS. 
o This algorithm is not optimal. 



2a. Write a program to implement Informed search techniques:   
Greedy Best First Search. 

 ''' 

from queue import PriorityQueue 
v = 14 
graph = [[] for i in range(v)] 
 
# Function For Implementing Best First Search 
# Gives output path having lowest cost 
 
 
def best_first_search(actual_Src, target, n): 
    visited = [False] * n 
    pq = PriorityQueue() 
    pq.put((0, actual_Src)) 
    visited[actual_Src] = True 
 
    while pq.empty() == False: 
        u = pq.get()[1] 
# Displaying the path having lowest cost 
        print(u, end=" ") 
        if u == target: 
            break 
 
    for v, c in graph[u]: 
        if visited[v] == False: 
            visited[v] = True 
            pq.put((c, v)) 
            print() 
 
# Function for adding edges to graph 
 
 
def addedge(x, y, heuristic): 
 
    graph[x].append((y, heuristic)) 
    graph[y].append((x, heuristic)) 
 
 
# The nodes shown in above example(by alphabets) are 
# implemented using integers addedge(x,y,heuristic); 
addedge(0, 1, 3) 
addedge(0, 2, 6) 
addedge(0, 3, 5) 
addedge(1, 4, 9) 
addedge(1, 5, 8) 
addedge(2, 6, 12) 
addedge(2, 7, 14) 
addedge(3, 8, 7) 
addedge(8, 9, 5) 
addedge(8, 10, 6) 
addedge(9, 11, 1) 
addedge(9, 12, 10) 
addedge(9, 13, 2) 
 
source = 0 
target = 9 
best_first_search(source, target, v)

'''
Output: 
 
0 1 3 2 8 9

'''