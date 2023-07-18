from Graph import Graph


def dfs_recursive(g, source, visited):
    result = str(source)
    visited[source] = True
    neighbor_head = g.graph[source].get_head()
    tmp = neighbor_head
    while tmp:
        if not visited[tmp.val]:
            result += dfs_recursive(g, tmp.val, visited)
        tmp = tmp.next
    return result

def main():
    G = Graph(4)
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    
    num_nodes = G.vertices
    visited = [False] * num_nodes
    # this is for only one source, do it for multiple sources if they are not visited in a loop
    res = dfs_recursive(G, 0, visited)
    print(res)
    
if __name__ == "__main__":
    main()