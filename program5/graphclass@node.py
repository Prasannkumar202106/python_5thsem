# Lab 5 Design a "Graph" class that represent a Graph#
# edges are represented as {Node1: (Node2, Weight1), Node2: (Node3, Weight2)}
class Graph: #declaring class
    def __init__(self):
        self.graph = dict()

    # edges are represented as 
    # {Node_1: (Node_2, Weight_1), Node_2: (Node_3, Weight_2)}
    def add(self, node, child, weight):
        self.graph[node] = (child, weight)

    def display(self):
        print(self.graph)

#driver code to display graph
ob = Graph()
ob.add(1, 2, 2)
ob.add(2, 3, 4)
ob.display()
