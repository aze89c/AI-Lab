'''2b A* Search Algorithm 
 
A* search is the most commonly known form of best-first search. It uses heuristic function h(n), and cost 
to reach the node n from the start state g(n). 
A* search algorithm finds the shortest path through the search space using the heuristic function. This search 
algorithm expands less search tree and provides optimal result faster. 
it uses g(n)+h(n) instead of g(n). 
Algorithm of A* search: 
Step1: Place the starting node in the OPEN list. 
Step 2: Check if the OPEN list is empty or not, if the list is empty then return failure and stops. 
Step 3: Select the node from the OPEN list which has the smallest value of evaluation function (g+h), if 
node n is goal node then return success and stop, otherwise 
Step 4: Expand node n and generate all of its successors, and put n into the closed list. For each successor n', 
check whether n' is already in the OPEN or CLOSED list, if not then compute evaluation function for n' and 
place into Open list. 
Step 5: Else if node n' is already in OPEN and CLOSED, then it should be attached to the back pointer 
which reflects the lowest g(n') value. 
Step 6: Return to Step 2. 
Advantages: 
o A* search algorithm is the best algorithm than other search algorithms. 
o A* search algorithm is optimal and complete. 
o This algorithm can solve very complex problems. 
Disadvantages: 
o It does not always produce the shortest path as it mostly based on heuristics and approximation. 
o A* search algorithm has some complexity issues. 
o The main drawback of A* is memory requirement as it keeps all generated nodes in the memory, so 
it is not practical for various large-scale problems. 
 
 
 
 
 
 
 
 
 
 
'''
 
# 2b. Write a Program to implement Informed search technique:  A* Algorithm 
 
 
def aStarAlgo(start_node, stop_node): 
 
    open_set = set(start_node) 
    closed_set = set() 
    g = {} #store distance from starting node 
    parents = {}# parents contains an adjacency map of all nodes 
 
#ditance of starting node from itself is zero 
    g[start_node] = 0 
#start_node is root node i.e it has no parent nodes 
#so start_node is set to its own parent node 
    parents[start_node] = start_node 
 
 
    while len(open_set) > 0: 
        n = None 
 
#node with lowest f() is found 
    for v in open_set: 
       if n == None or g[v] + heuristic(v) < g[n] + heuristic(n): 
            n = v 
 
 
            if n == stop_node or Graph_nodes[n] == None: 
                pass 
            else: 
                for (m, weight) in get_neighbors(n): 
#nodes 'm' not in first and last set are added to first 
#n is set its parent 
                    if m not in open_set and m not in closed_set: 
                        open_set.add(m) 
 
 
            parents[m] = n 
            g[m] = g[n] + weight 
 
 
#for each node m,compare its distance from start i.e g(m) to the 
#from start through n node 
    else: 
        if g[m] > g[n] + weight: 
#update g(m) 
            g[m] = g[n] + weight 
#change parent of m to n 
            parents[m] = n 
 
#if m in closed set,remove and add to open 
        if m in closed_set: 
            closed_set.remove(m) 
            open_set.add(m) 
 
        if n == None: 
            print('Path does not exist!') 
            return None 
 
# if the current node is the stop_node 
# then we begin reconstructin the path from it to the start_node 
        if n == stop_node: 
            path = [] 
 
        while parents[n] != n: 
            path.append(n) 
            n = parents[n] 
 
        path.append(start_node) 
 
        path.reverse() 
 
 
 
  
    print('Path found: {}'.format(path)) 
    return path 
 
 
# remove n from the open_list, and add it to closed_list 
# because all of his neighbors were inspected 
    open_set.remove(n) 
    closed_set.add(n) 
 
    print('Path does not exist!') 
    return None 
 
#define fuction to return neighbor and its distance 
#from the passed node 
def get_neighbors(v): 
    if v in Graph_nodes: 
        return Graph_nodes[v] 
    else: 
        return None 
#for simplicity we ll consider heuristic distances given 
#and this function returns heuristic distance for all nodes 
def heuristic(n): 
    H_dist = { 
'A': 11, 
'B': 6, 
'C': 99, 
'D': 1, 
'E': 7, 
'G': 0, 
 
} 
 
    return H_dist[n] 
 
 
 
#Describe your graph here 
Graph_nodes = { 
'A': [('B', 2), ('E', 3)], 
'B': [('C', 1),('G', 9)], 
'C': None, 
'E': [('D', 6)], 
'D': [('G', 1)], 
 
} 
aStarAlgo('A', 'G') 
 
 
 
 
 
'''
Output: 
 
Path Found: [ 'A','E','D','G']
'''