graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def dfs_traversal(visited, graph, node): 
    visited.append(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_traversal(visited, graph, neighbour)

def print_leaf_nodes_dfs(visited, graph, node): 
    visited.append(node)

    # Check if the node is a leaf node
    if not graph[node]:
        print(node, end=" ")
    else:
        for neighbour in graph[node]:
            if neighbour not in visited:
                print_leaf_nodes_dfs(visited, graph, neighbour)

# Driver Code
print("DFS Traversal order:")
dfs_traversal([], graph, '5')
print("\nLeaf nodes in the graph are:")
print_leaf_nodes_dfs([], graph, '5')