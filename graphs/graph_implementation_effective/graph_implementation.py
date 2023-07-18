from Graph import Graph

def main():
    G = Graph(4)
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)

    G.print_graph()
    
if __name__ == "__main__":
    main()
