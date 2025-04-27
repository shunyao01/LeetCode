from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def dfs_iter(self, node):
        """
        Stack for DFS, LIFO
        Time Complexity: O(V+E)
        Deque pop
        """
        visited = set() # visit
        stack = deque([node]) # explore
        res = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                res.append(node.value)

                for neighbor in reversed(node.neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return res


    def dfs_rec(self, node):
        """
        Perform DFS search
        
        Time complexity: O(V+E)
        """
        visited = set()
        res = []
        res = self.dfs_visit(node, visited, res)

        return res

    def dfs_visit(self, node, visited, res):
        
        if node not in visited:
            visited.add(node)
            res.append(node.value)

            for neighbor in node.neighbors:
                res = self.dfs_visit(neighbor, visited, res)

        return res


# Create nodes
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

# Connect nodes
a.add_neighbor(b)
a.add_neighbor(c)
b.add_neighbor(d)
b.add_neighbor(e)
c.add_neighbor(f)

# Create a graph and add nodes
graph = Graph()
graph.add_node(a)
graph.add_node(b)
graph.add_node(c)
graph.add_node(d)
graph.add_node(e)
graph.add_node(f)

if __name__ == '__main__':
    print(graph.dfs_iter(a))
    print(graph.dfs_rec(a))