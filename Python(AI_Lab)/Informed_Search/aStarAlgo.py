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
    open_set = set([start_node])  # Set of nodes to be evaluated
    closed_set = set()  # Set of nodes already evaluated
    g = {}  # Store distance from the start node
    parents = {}  # Stores the parent of each node

    # Distance of start_node from itself is zero
    g[start_node] = 0

    # Start_node is its own parent
    parents[start_node] = None

    while len(open_set) > 0: 
        n = None 

        # Find the node with the lowest f(n) = g(n) + h(n)
        for node in open_set: 
            if n is None or g[node] + heuristic(node) < g[n] + heuristic(n): 
                n = node

        # If no node is found, path does not exist
        if n is None:
            print('Path does not exist!')
            return None

        # If the goal node is reached, reconstruct the path
        if n == stop_node: 
            path = [] 
            while n is not None: 
                path.append(n) 
                n = parents[n] 
            path.reverse() 
            print('Path found: {}'.format(path)) 
            return path 

        # For all neighbors of the current node
        for (neighbor, weight) in get_neighbors(n): 
            if neighbor not in open_set and neighbor not in closed_set: 
                open_set.add(neighbor) 
                parents[neighbor] = n 
                g[neighbor] = g[n] + weight 
            else: 
                # Update g(neighbor) if a shorter path is found
                if g[neighbor] > g[n] + weight: 
                    g[neighbor] = g[n] + weight 
                    parents[neighbor] = n 

                    # If the neighbor is in closed_set, move it to open_set
                    if neighbor in closed_set: 
                        closed_set.remove(neighbor) 
                        open_set.add(neighbor) 

        # Remove n from open_set and add it to closed_set
        open_set.remove(n) 
        closed_set.add(n) 

    print('Path does not exist!')
    return None 

# Define function to return neighbors and their distances
def get_neighbors(v): 
    if v in Graph_nodes: 
        return Graph_nodes[v] 
    else: 
        return []

# Heuristic function (predefined heuristic distances)
def heuristic(n): 
    H_dist = { 
        'A': 11, 
        'B': 6, 
        'C': 99, 
        'D': 1, 
        'E': 7, 
        'G': 0, 
    } 
    return H_dist.get(n, float('inf'))  # Return infinity if node is not in H_dist

# Describe the graph
Graph_nodes = { 
    'A': [('B', 2), ('E', 3)], 
    'B': [('C', 1), ('G', 9)], 
    'C': [], 
    'E': [('D', 6)], 
    'D': [('G', 1)], 
} 

# Run the A* Algorithm
aStarAlgo('A', 'G')
 
 
 
 
'''
Output: 
 
Path Found: [ 'A','E','D','G']
'''