# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Return a deepcopy of graph using datatype node

        Args:
            Nodde: contain val and neighours as list

        Return:
            A copy version of the node

        Edge case:
            0 node
            1 node

        Handle original and copy pointer, Queue stores original, Clones stores clone
        Pop from queue -> Explore neighbor -> if not cloned, add queue & clone neighbor & add hashmap -> LINK neighbor to source node
        Copy the link/edge, regardless the node is cloned or not before, bidirectional graph! New edge to existing node!

        Trick: hashmap to keep track of already created node, acknowledge all edges
        """
        # empty graph: 0 node
        if node is None: return node
        
        q = deque([node])
        clones = {node.val : Node(node.val, [])}

        while q:
            cur = q.popleft() # current node
            cur_clone = clones[cur.val] # clone node

            # for each neigbour, if not visited, create a new clone, link current to new, add to hashmap, append to q
            for neighbor in cur.neighbors:
                if neighbor.val not in clones:
                    
                    # create new neighbor clone and add to hashmap
                    clones[neighbor.val] = Node(neighbor.val)
                    
                    # add new clone to q to be explored
                    q.append(neighbor)
                
                # link new clone to its parent node
                # even if the node is cloned before, we need to add link, because we want copy edges not visit & output
                cur_clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]