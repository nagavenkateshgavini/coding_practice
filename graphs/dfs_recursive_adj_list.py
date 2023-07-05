def dfs_recursive(adj_list, node, visited):
    visited[node] = True
    num_nodes = len(adj_list.keys())
    print(node)
    
    for new_node in adj_list[node]:
        if not visited[new_node] and adj_list[new_node]:
            dfs_recursive(adj_list, new_node, visited)

def main():
    adj_list = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 4],
        3: [1, 4],
        4: [2, 3, 5],
        5: [4, 6],
        6: [5]
    }
    
    num_nodes = len(adj_list.keys())
    visited = [False] * num_nodes
    dfs_recursive(adj_list, 0, visited)

if __name__ == "__main__":
    main()