#1.Constructor and Add vertex method

class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        #We put an if condition to not include duplicate values
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
my_graph = Graph()

my_graph.add_vertex("A")

my_graph.print_graph()

#Output
"""

A : []

"""

#2.Add edge method

class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1 ,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1,2)

my_graph.print_graph()

#Output
"""

1 : [2]
2 : [1]

"""

#3.Remove edge method
#Case 1:

class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1 ,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False
    
my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")

my_graph.add_edge("A","B")
my_graph.add_edge("B","C")
my_graph.add_edge("C","A")

my_graph.print_graph()

my_graph.remove_edge("A","B")

my_graph.print_graph()

#Output
"""

A : ['B', 'C']
B : ['A', 'C']
C : ['B', 'A']
A : ['C']
B : ['C']
C : ['B', 'A']

"""

#Case 2:

class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1 ,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            #When a vertex v2 exists in adj_list, but doesn't have an edge with vertex v1, it raises a ValueError. Hence, we use
            #Exception Handling technique here
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A","B")
my_graph.add_edge("B","C")
my_graph.add_edge("C","A")

my_graph.print_graph()

my_graph.remove_edge("A","D")

my_graph.print_graph()

#Output
"""

A : ['B', 'C']
B : ['A', 'C']
C : ['B', 'A']
D : []
A : ['B', 'C']
B : ['A', 'C']
C : ['B', 'A']
D : []

"""

#4.Remove vertex method

class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1 ,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    
my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("A","D")
my_graph.add_edge("B","D")
my_graph.add_edge("C","D")

my_graph.print_graph()

my_graph.remove_vertex("D")

my_graph.print_graph()

#Output
"""

A : ['B', 'C', 'D']
B : ['A', 'D']
C : ['A', 'D']
D : ['A', 'B', 'C']
A : ['B', 'C']
B : ['A']
C : ['A']

"""