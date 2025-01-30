class Node:
    def __init__(self, values):
        self.values = values  # List of 5 integers
        self.children = []
        self.additional_value = None  # Additional value to be recorded

def dfs(node, visited=None):
    if visited is None:
        visited = set()
    
    if node in visited:
        return
    
    visited.add(node)
    
    # Record another value for this node (example: sum of values)
    node.additional_value = sum(node.values)
    print(f"Node values: {node.values}, Additional value: {node.additional_value}")
    
    for child in node.children:
        dfs(child, visited)
#game example
# Example usage
# will use a dfs to simulate a game tree
root = Node([1, 2, 3, 4, 5])

dfs(root)