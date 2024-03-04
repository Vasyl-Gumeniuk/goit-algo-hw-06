import networkx as nx
import matplotlib.pyplot as plt

# Створення пустого графа
G = nx.Graph()

# Додавання вершин (міст)
G.add_nodes_from(["Місто 1", "Місто 2", "Місто 3", "Місто 4", "Місто 5", "Місто 6", "Місто 7", "Місто 8", "Місто 9", "Місто 10"])

# Додавання ребер (вулиць) з вагами
edges = [("Місто 1", "Місто 2", 10), ("Місто 1", "Місто 3", 5), ("Місто 2", "Місто 3", 7), ("Місто 3", "Місто 4", 3), ("Місто 4", "Місто 5", 5), ("Місто 6", "Місто 5", 3), ("Місто 5", "Місто 1", 14), ("Місто 7", "Місто 6", 3), ("Місто 8", "Місто 7", 6), ("Місто 9", "Місто 8", 2), ("Місто 10", "Місто 9", 3), ("Місто 7", "Місто 10", 6)]
G.add_weighted_edges_from(edges)

# Візуалізація графа
pos = nx.spring_layout(G)  # Позиція вершин для візуалізації
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=12, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels={(i, j): G[i][j]['weight'] for i, j in G.edges()}, font_color='red')
plt.show()



def main():
    # Аналіз основних характеристик графа
    print("Кількість вершин (міст):", G.number_of_nodes())
    print("Кількість ребер (вулиць):", G.number_of_edges())
    print("Список вершин (міст):", list(G.nodes()))
    print("Список ребер (вулиць):", list(G.edges()))
    print("Ступінь вершин:")
    for node in G.nodes():
        print(f"{node}: {nx.degree(G, node)}")




if __name__ == "__main__":
    main()
