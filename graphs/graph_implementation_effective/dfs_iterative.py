from Graph import Graph
from stack_with_list import stack

def dfs_iterative(g, source):
    num_nodes = g.vertices
    visited = [False] * num_nodes
    s = stack()
    s.push(source)
    
    res = []
    while not s.isEmpty():
        print(s.elements, res)
        s_top = s.top()
        res.append(str(s_top))
        visited[s_top] = True
        s.pop()
        
        neighbors_head = g.graph[s_top].get_head()
        tmp = neighbors_head
        while tmp:
            if not visited[tmp.val]:
                s.push(tmp.val)
            tmp = tmp.next
       
    return "".join(res)

def main():
    G = Graph(4)
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    
    res = dfs_iterative(G, 0)
    print(res)

if __name__ == "__main__":
    main()