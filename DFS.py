mygraph = {
    'A': ['D', 'B'],
    'B': ['C', 'G', 'E'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['F', 'G']
}

def myDFS(mygraph, startnode, endnode, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(startnode)
    print(startnode, end=" ")
    
    if startnode == endnode:
        print(f"\nEnd node '{endnode}' found")
        return True
    
    for neighbor in mygraph.get(startnode, []):
        if neighbor not in visited:
            if myDFS(mygraph, neighbor, endnode, visited):
                return True
    
    return False

start_node = input('Enter the starting node: ')
end_node = input('Enter the end node: ')

if start_node not in mygraph or end_node not in mygraph:
    print("One or both nodes are not in the graph.")
else:
    if not myDFS(mygraph, start_node, end_node):
        print(f"\nEnd node '{end_node}' was not reachable from '{start_node}'.")