from LinkedList import LinkedList

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        for vertex in range(self.vertices):
            self.graph.append(LinkedList())
    
    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.graph[source].insert_at_head(destination)
            # self.graph[destination].insert_at_head(source)

    def print_graph(self):
        for i in range(self.vertices):
            print(f"{i} || ", end="")
            node_head = self.graph[i].get_head()
            head_tmp = node_head
            while head_tmp:
                print(head_tmp.val, end="->")
                head_tmp = head_tmp.next
            print("None")
