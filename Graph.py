class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, nodeTag):
        self.nodes[nodeTag] = Node()

    def joinNodes(self, node1, node2):
        newNode = Node()

        self.nodes[node1] = newNode
        self.nodes[node2] = newNode
    
    def addEdge(self, node1,node2):
        self.nodes[node1].adjacent.append(node2)

    def DFS(self,nodeName):
        node = self.nodes[nodeName]
        biggest = self.DFS_aux(node, 0)
        node.longestPath = biggest
        
    def DFS_aux(self,node,longestSoFar):
        biggest = longestSoFar
        for a in node.adjacent:
            currentNode = self.nodes[a]
            current = self.DFS_aux(currentNode,longestSoFar + 1)
            biggest = max(biggest,current)
        
        return biggest

class Node:
    def __init__(self):
        self.adjacent = []
        self.longestPath = 0