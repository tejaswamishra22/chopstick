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

# Example usage
root = Node([1, 2, 3, 4, 5])
child1 = Node([6, 7, 8, 9, 10])
child2 = Node([11, 12, 13, 14, 15])
child3 = Node([16, 17, 18, 19, 20])

root.children.append(child1)
root.children.append(child2)
child1.children.append(child3)

dfs(root)