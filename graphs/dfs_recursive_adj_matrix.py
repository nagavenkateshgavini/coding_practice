def dfs_recursive(matrix, start_node, visited):
    visited[start_node] = True
    num_nodes = len(matrix)
    print(start_node)
    
    for i in range(num_nodes):
        if matrix[start_node][i] == 1 and not visited[i]:
            dfs_recursive(matrix, i, visited)

def main():    
    adj_matrix = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 0]
    ]
    
    num_nodes = len(adj_matrix)
    visited = [False] * num_nodes
    dfs_recursive(adj_matrix, 0, visited)

if __name__ == "__main__":
    main()