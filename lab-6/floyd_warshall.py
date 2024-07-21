def floyd_warshall(graph):
    # Number of vertices in the graph
    V = len(graph)
    
    # Initialize the solution matrix same as input graph matrix
    dist = [[float('inf')] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
    
    # Set the diagonal elements to 0
    for i in range(V):
        dist[i][i] = 0

    # Add vertices individually. Update the distances using three nested loops
    for k in range(V):
        print(f"Intermediate distance matrix after considering vertex {k}:")
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        
        # Print the current state of the distance matrix
        for row in dist:
            print(row)
        print()  # Print a blank line for better readability
    
    # Return the final result
    return dist

# Example usage:
INF = float('inf')
graph = [
    [0, 3, INF, INF],
    [2, 0, INF, INF],
    [INF, 7, 0, 1],
    [6, INF, INF, 0]
]

dist = floyd_warshall(graph)

print("Final shortest distance matrix:")
for row in dist:
    print(row)
