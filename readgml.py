import networkx as nx

def print_edge_list_with_default_ids(gml_file):
    G = nx.read_gml(gml_file)
    
    node_index_mapping = {node: idx for idx, node in enumerate(G.nodes())}
    
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()

    with open(output_file, "w") as file:
        file.write(f"{num_nodes} {num_edges}\n")

        for edge in G.edges():
            source_idx = node_index_mapping[edge[0]]
            target_idx = node_index_mapping[edge[1]]
            file.write(f"{source_idx} {target_idx}\n")
    
    communities = {frozenset(G.nodes[v]["community"]) for v in G}

    print(communities)

gml_file = "dolphins.gml"
output_file = "dolphins.txt"

print_edge_list_with_default_ids(gml_file)


