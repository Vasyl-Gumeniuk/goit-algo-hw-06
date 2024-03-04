import time
import networkx as nx


# Завантаження графа
G = nx.Graph()
G.add_nodes_from(["Місто 1", "Місто 2", "Місто 3", "Місто 4", "Місто 5", "Місто 6", "Місто 7", "Місто 8", "Місто 9", "Місто 10"])
edges = [("Місто 1", "Місто 2"), ("Місто 1", "Місто 3"), ("Місто 2", "Місто 3"), ("Місто 3", "Місто 4"), ("Місто 4", "Місто 5"), ("Місто 6", "Місто 5"), ("Місто 5", "Місто 1"), ("Місто 7", "Місто 6"), ("Місто 8", "Місто 7"), ("Місто 9", "Місто 8"), ("Місто 10", "Місто 9"), ("Місто 7", "Місто 10")]
G.add_edges_from(edges)


# Алгоритм DFS
def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = dfs(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


# Алгоритм BFS
def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in graph[vertex] - set(path):
            if next_node == end:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))



# Перетворення графу NetworkX у словникове представлення
graph_dict = {node: set(G.neighbors(node)) for node in G.nodes()}

# Визначення початкової та кінцевої вершин
start_node = "Місто 1"
end_node = "Місто 10"


def main():

    # Вимірювання часу для алгоритму DFS
    start_time = time.time()
    dfs_paths = dfs(graph_dict, start_node, end_node)
    dfs_time = time.time() - start_time

    print("DFS Paths:")
    for path in dfs_paths:
        print(path)
    print(f"Час виконання DFS: {dfs_time: .10F}")

    # Вимірювання часу для алгоритму BFS
    start_time = time.time()
    bfs_paths = list(bfs(graph_dict, start_node, end_node))
    bfs_time = time.time() - start_time

    print("\nBFS Paths:")
    for path in bfs_paths:
        print(path)
    print(f"Час виконання BFS: {bfs_time: .10F}")

    # Вимірювання часу для вбудованого алгоритму DFS з бібліотеки NetworkX
    start_time = time.time()
    nx_dfs_paths = list(nx.all_simple_paths(G, source=start_node, target=end_node))
    nx_dfs_time = time.time() - start_time

    print("\nШляхи DFS від NetworkX:")
    for path in nx_dfs_paths:
        print(path)
    print(f"Час виконання DFS від NetworkX: {nx_dfs_time: .10F}")

    # Вимірювання часу для вбудованого алгоритму BFS з бібліотеки NetworkX
    start_time = time.time()
    nx_bfs_paths = list(nx.all_shortest_paths(G, source=start_node, target=end_node))
    nx_bfs_time = time.time() - start_time

    print("\nШляхи BFS від NetworkX:")
    for path in nx_bfs_paths:
        print(path)
    print(f"Час виконання BFS від NetworkX: {nx_bfs_time: .10F}")




if __name__ == "__main__":
    main()
