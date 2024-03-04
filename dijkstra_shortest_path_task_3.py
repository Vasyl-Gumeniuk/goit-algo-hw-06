import networkx as nx
import matplotlib.pyplot as plt
import random

# Створення графа
G = nx.Graph()

# Додавання вершин (міст)
G.add_nodes_from(["Місто 1", "Місто 2", "Місто 3", "Місто 4", "Місто 5", "Місто 6", "Місто 7", "Місто 8", "Місто 9", "Місто 10"])

# Додавання ребер (вулиць) з вагами
edges = [("Місто 1", "Місто 2", 10), ("Місто 1", "Місто 3", 5), ("Місто 2", "Місто 3", 7), ("Місто 3", "Місто 4", 3), ("Місто 4", "Місто 5", 5), ("Місто 6", "Місто 5", 3), ("Місто 5", "Місто 1", 14), ("Місто 7", "Місто 6", 3), ("Місто 8", "Місто 7", 6), ("Місто 9", "Місто 8", 2), ("Місто 10", "Місто 9", 3), ("Місто 7", "Місто 10", 6)]
G.add_weighted_edges_from(edges)

# Функція для знаходження найкоротших шляхів між всіма вершинами
def all_pairs_shortest_path(G):
    all_paths = dict(nx.all_pairs_dijkstra_path(G))
    all_lengths = dict(nx.all_pairs_dijkstra_path_length(G))
    return all_paths, all_lengths

# Знаходження найкоротших шляхів
all_paths, all_lengths = all_pairs_shortest_path(G)



def main():
    # Виведення результатів
    print("Найкоротші шляхи між вершинами:")
    for source in all_paths:
        for target in all_paths[source]:
            if source != target:
                path = all_paths[source][target]
                length = all_lengths[source][target]
                print(f"Шлях з {source} до {target}: {path}, довжина = {length}")




if __name__ == "__main__":
    main()
