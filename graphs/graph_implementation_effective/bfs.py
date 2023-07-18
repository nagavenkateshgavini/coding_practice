from Graph import Graph
from queue_with_list import queue

def bfs_traversal(g, source):
    num_nodes = g.vertices
    visited = [False] * num_nodes
    myqueue = queue()
    myqueue.enqueue(source)
    visited[myqueue.top()] = True
    
    result = ""
    while not myqueue.is_empty():
        top = myqueue.top()
        result += str(top)
        myqueue.dequeue()
        
        neighbors_head = g.graph[top].get_head()
        tmp = neighbors_head
        while tmp:
            if not visited[tmp.val]:
                myqueue.enqueue(tmp.val)
                visited[tmp.val] = True
            tmp = tmp.next
        
    return result

def main():
    G = Graph(4)
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    
    res = bfs_traversal(G, 0)
    print(res)
    
if __name__ == "__main__":
    main()
