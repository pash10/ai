Sure, I'll split the BFS function into two separate functions:

    bfs_traversal: This will print each node in BFS order.
    print_leaf_nodes: This will print only the leaf nodes (end points) of the graph.

Here's the modified code:

python
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []   # Initialize a queue

def bfs_traversal(visited, graph, node): # function for BFS traversal
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print(m, end=" ")
    
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

def print_leaf_nodes(visited, graph, node): # function to print leaf nodes
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)
    
    # Check if the node is a leaf node
    if not graph[m]:
        print(m, end=" ")
    else:
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
print("BFS Traversal order:")
bfs_traversal([], graph, '5')
print("\nLeaf nodes in the graph are:")
print_leaf_nodes([], graph, '5')