import networkx as nx
from networkx.generators.community import LFR_benchmark_graph

n = 250
tau1 = 3
tau2 = 1.5
mu = 0.1
G = LFR_benchmark_graph(
    n, tau1, tau2, mu, average_degree=5, min_community=20, seed=
)

# Output the number of nodes and edges
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

# Output the edge list
edge_list = list(G.edges())

# Print in the desired format
print(f"{num_nodes} {num_edges}")
for edge in edge_list:
    print(f"{edge[0]} {edge[1]}")

communities = {frozenset(G.nodes[v]["community"]) for v in G}