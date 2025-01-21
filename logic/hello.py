class Node:
    def __init__(self, values):
        self.values = values  # List of 5 integers
        self.children = []

def dfs(node, visited=None):
    if visited is None:
        set.add(node);
    
    if node in visited:
        return
    
    visited.add(node)
    
    for child in node.children:
        dfs(child, visited)

# Example usage
root = Node([0, 0, 0, 0, 0])
my_set = set()
set.add(root)
dfs(root)