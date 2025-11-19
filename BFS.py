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

def myBFS(mygraph, startnode, endnode):
    visited = set()
    queue = [startnode]
    visited.add(startnode)
    
    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")
        
        if current_node == endnode:
            print(f"\nEnd node '{endnode}' found!")
            return True

        for neighbor in mygraph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    print(f"\nEnd node '{endnode}' was not reachable from '{startnode}'.")
    return False

start_node = input('Enter the starting node: ')
end_node = input('Enter the end node: ')

if start_node not in mygraph or end_node not in mygraph:
    print("One or both nodes are not in the graph.")
else:
    myBFS(mygraph, start_node, end_node)