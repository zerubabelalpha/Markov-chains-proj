import networkx as nx

def build_graph(file_path):
    
    print(f"Loading graph from {file_path}...")
    # The file has lines like "FromNodeId\tToNodeId" and comments starting with '#'
    G = nx.read_edgelist(file_path, create_using=nx.DiGraph(), nodetype=int, comments='#')
    print(f"Graph loaded successfully.")
    print(f"Number of Nodes: {G.number_of_nodes()}")
    print(f"Number of Edges: {G.number_of_edges()}")
    return G
